import asyncio
import os
from datetime import UTC, datetime

from sqlalchemy import select

from app.core.database import SessionFactory, dispose_engine
from app.models.assets import Asset, AssetStatus, AssetType, ExposureLevel
from app.models.evaluations import (
    Answer,
    Evaluation,
    EvaluationAsset,
    FrameworkCategory,
    FrameworkControl,
    FrameworkFunction,
    Question,
)
from app.models.identity import Membership, Organization, RoleCode, User
from app.models.operations import Incident, IncidentSeverity, Notification
from app.models.risks import (
    Risk,
    RiskLevel,
    RiskStatus,
    RiskTreatment,
    Threat,
    TreatmentStrategy,
    Vulnerability,
)
from app.security.passwords import hash_password
from app.standards.nist_csf import seed_nist_csf

DEMO_USERS = (
    ("administrador@demo.local", "Responsable SGSI", RoleCode.ORG_ADMIN),
    ("analista@demo.local", "Analista de Seguridad TI", RoleCode.ANALYST),
    ("consulta@demo.local", "Auditor Académico", RoleCode.VIEWER),
)


async def seed() -> None:
    password = os.getenv("DEMO_PASSWORD")
    if not password or len(password) < 12:
        raise RuntimeError("Defina DEMO_PASSWORD con al menos 12 caracteres")
    async with SessionFactory() as db:
        framework = await seed_nist_csf(db)
        organization = await db.scalar(
            select(Organization).where(Organization.slug == "universidad-ficticia-valle-verde")
        )
        if organization is None:
            organization = Organization(
                name="Universidad Ficticia del Valle Verde (UFVV)",
                slug="universidad-ficticia-valle-verde",
                sector="Educación superior",
                size="4,500 estudiantes y 450 colaboradores (supuesto académico)",
                country="GT",
            )
            db.add(organization)
            await db.flush()

        # Preserve existing organizations as separate tenants. The selector lists
        # the active organizations for which the user has an active membership.
        for email, full_name, role in DEMO_USERS:
            user = await db.scalar(select(User).where(User.email == email))
            if user is None:
                user = User(
                    email=email,
                    full_name=full_name,
                    password_hash=hash_password(password),
                    is_active=True,
                )
                db.add(user)
                await db.flush()
            if email == "administrador@demo.local":
                user.is_superadmin = True
                user.is_active = True
                user.password_hash = hash_password(password)
                user.failed_login_attempts = 0
                user.locked_until = None
            membership = await db.scalar(
                select(Membership).where(
                    Membership.organization_id == organization.id,
                    Membership.user_id == user.id,
                )
            )
            if membership is None:
                db.add(
                    Membership(
                        organization_id=organization.id,
                        user_id=user.id,
                        role_code=role,
                    )
                )
        creator = await db.scalar(select(User).where(User.email == "administrador@demo.local"))
        assert creator is not None
        demo_assets = (
            ("Correo y colaboración institucional", "APP-MAIL-01", AssetType.APPLICATION, 5),
            ("Sistema de información estudiantil", "APP-SIS-01", AssetType.APPLICATION, 5),
            ("Estación de trabajo de Registro Académico", "PC-REG-01", AssetType.COMPUTER, 4),
            ("Firewall perimetral del campus", "NET-FW-01", AssetType.NETWORK, 5),
            ("Base de datos de expedientes y calificaciones", "DB-EST-01", AssetType.DATABASE, 5),
            ("Servicio institucional de identidad", "APP-ID-01", AssetType.CLOUD_SERVICE, 5),
            ("Plataforma virtual de aprendizaje", "APP-LMS-01", AssetType.APPLICATION, 5),
            ("Repositorio cifrado de respaldos Azure", "CLD-BKP-01", AssetType.CLOUD_SERVICE, 5),
        )
        for name, code, asset_type, criticality in demo_assets:
            exists = await db.scalar(
                select(Asset.id).where(
                    Asset.organization_id == organization.id,
                    Asset.internal_code == code,
                )
            )
            if exists is None:
                db.add(
                    Asset(
                        organization_id=organization.id,
                        created_by=creator.id,
                        name=name,
                        internal_code=code,
                        asset_type=asset_type,
                        description="Dato ficticio para demostración",
                        exposure_level=ExposureLevel.INTERNAL,
                        status=AssetStatus.ACTIVE,
                        confidentiality_criticality=criticality,
                        integrity_criticality=criticality,
                        availability_criticality=criticality,
                        overall_criticality=criticality,
                        tags=["demo", "ficticio"],
                        outgoing_dependencies=[],
                    )
                )
        await db.flush()
        threat = await db.scalar(
            select(Threat).where(
                Threat.organization_id == organization.id,
                Threat.name == "Phishing dirigido a cuentas de docentes",
            )
        )
        if threat is None:
            threat = Threat(
                organization_id=organization.id,
                created_by=creator.id,
                name="Phishing dirigido a cuentas de docentes",
                description="Escenario ficticio de robo de credenciales institucionales.",
                likelihood=4,
            )
            db.add(threat)
        vulnerability = await db.scalar(
            select(Vulnerability).where(
                Vulnerability.organization_id == organization.id,
                Vulnerability.name == "MFA no exigida a cuentas privilegiadas",
            )
        )
        if vulnerability is None:
            vulnerability = Vulnerability(
                organization_id=organization.id,
                created_by=creator.id,
                name="MFA no exigida a cuentas privilegiadas",
                description=(
                    "Supuesto académico: acceso de alto impacto sin segundo factor obligatorio."
                ),
                severity=4,
            )
            db.add(vulnerability)
        await db.flush()
        demo_risk = await db.scalar(
            select(Risk).where(
                Risk.organization_id == organization.id,
                Risk.code == "RSK-DEMO-001",
            )
        )
        if demo_risk is None:
            mail_asset = await db.scalar(
                select(Asset).where(
                    Asset.organization_id == organization.id,
                    Asset.internal_code == "APP-MAIL-01",
                )
            )
            assert mail_asset is not None
            demo_risk = Risk(
                organization_id=organization.id,
                created_by=creator.id,
                code="RSK-DEMO-001",
                title="Compromiso de cuenta docente mediante phishing",
                description=(
                    "Escenario ficticio para demostrar priorización y tratamiento en la UFVV."
                ),
                asset_id=mail_asset.id,
                threat_id=threat.id,
                vulnerability_id=vulnerability.id,
                probability=4,
                impact=5,
                inherent_score=20,
                inherent_level=RiskLevel.CRITICAL,
                existing_controls="Filtro antispam y capacitación inicial.",
                residual_probability=2,
                residual_impact=4,
                residual_score=8,
                residual_level=RiskLevel.MEDIUM,
                treatment_strategy=TreatmentStrategy.MITIGATE,
                responsible_user_id=creator.id,
                progress=35,
                status=RiskStatus.IN_TREATMENT,
            )
            db.add(demo_risk)
            await db.flush()
            db.add(
                RiskTreatment(
                    organization_id=organization.id,
                    risk_id=demo_risk.id,
                    created_by=creator.id,
                    action="Habilitar MFA y ejecutar una simulación de phishing.",
                    responsible_user_id=creator.id,
                    progress=35,
                    notes="Acción ficticia de demostración.",
                )
            )
        demo_evaluation = await db.scalar(
            select(Evaluation).where(
                Evaluation.organization_id == organization.id,
                Evaluation.code == "UFVV-NIST-2026",
                Evaluation.version == 1,
            )
        )
        if demo_evaluation is None:
            asset_ids = list(
                (
                    await db.scalars(
                        select(Asset.id).where(Asset.organization_id == organization.id)
                    )
                ).all()
            )
            demo_evaluation = Evaluation(
                organization_id=organization.id,
                created_by=creator.id,
                framework_id=framework.id,
                code="UFVV-NIST-2026",
                name="Evaluación NIST CSF 2.0 de la UFVV",
                scope="Toda la organización; datos exclusivamente ficticios.",
                target_maturity=3,
                comments="Evaluación ficticia para explorar el MVP.",
                assets=[],
                answers=[],
            )
            db.add(demo_evaluation)
            await db.flush()
            demo_evaluation.assets.extend(
                EvaluationAsset(
                    organization_id=organization.id,
                    evaluation_id=demo_evaluation.id,
                    asset_id=asset_id,
                )
                for asset_id in asset_ids
            )
            question_ids = list(
                (
                    await db.scalars(
                        select(Question.id)
                        .join(FrameworkControl)
                        .join(FrameworkCategory)
                        .join(FrameworkFunction)
                        .where(FrameworkFunction.framework_id == framework.id)
                    )
                ).all()
            )
            demo_evaluation.answers.extend(
                Answer(
                    organization_id=organization.id,
                    evaluation_id=demo_evaluation.id,
                    question_id=question_id,
                    answered_by=creator.id,
                    maturity=2,
                    comment="Respuesta ficticia de demostración.",
                )
                for question_id in question_ids
            )
        incident = await db.scalar(
            select(Incident).where(
                Incident.organization_id == organization.id,
                Incident.title == "Intento de acceso sospechoso (demostración)",
            )
        )
        if incident is None:
            db.add(
                Incident(
                    organization_id=organization.id,
                    created_by=creator.id,
                    title="Intento de acceso sospechoso a expediente estudiantil (demostración)",
                    description=(
                        "Evento ficticio para demostrar la gestión universitaria de incidentes."
                    ),
                    severity=IncidentSeverity.MEDIUM,
                    occurred_at=datetime.now(UTC),
                )
            )
        notification = await db.scalar(
            select(Notification).where(
                Notification.organization_id == organization.id,
                Notification.user_id == creator.id,
                Notification.title == "Bienvenido al MVP",
            )
        )
        if notification is None:
            db.add(
                Notification(
                    organization_id=organization.id,
                    user_id=creator.id,
                    title="Bienvenido al MVP",
                    message="Revise los indicadores y acciones ficticias de demostración.",
                    link="/panel",
                )
            )
        await db.commit()
    await dispose_engine()
    print("Seed demostrativo completo creado o actualizado.")


if __name__ == "__main__":
    asyncio.run(seed())
