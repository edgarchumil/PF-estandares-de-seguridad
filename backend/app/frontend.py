from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles


def mount_frontend(app: FastAPI, directory: Path) -> None:
    root = directory.resolve()
    if not (root / "index.html").is_file():
        raise RuntimeError("Frontend build is missing index.html")
    app.mount("/assets", StaticFiles(directory=root / "assets"), name="frontend-assets")

    @app.get("/{path:path}", include_in_schema=False)
    async def frontend(path: str) -> FileResponse:
        if path == "api" or path.startswith("api/"):
            raise HTTPException(status_code=404, detail="Not Found")
        target = (root / path).resolve()
        if target != root and root not in target.parents:
            raise HTTPException(status_code=404, detail="Not Found")
        if target.is_file():
            return FileResponse(target)
        if Path(path).suffix:
            raise HTTPException(status_code=404, detail="Not Found")
        return FileResponse(root / "index.html", headers={"Cache-Control": "no-cache"})
