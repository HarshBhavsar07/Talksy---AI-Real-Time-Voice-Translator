from fastapi import FastAPI, UploadFile, File, Form, Request
from fastapi.responses import JSONResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

import shutil
from pathlib import Path
from uuid import uuid4

from final import process_audio

app = FastAPI()

# ================= BASE PATH =================
BASE_DIR = Path(__file__).resolve().parent

# ================= STATIC =================
app.mount("/static", StaticFiles(directory=str(BASE_DIR / "static")), name="static")

# ================= TEMPLATES (ONLY THIS — NO CUSTOM ENV) =================
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))

# ================= DIRECTORIES =================
TEMP_DIR = BASE_DIR / "temp_audio"
AUDIO_DIR = BASE_DIR / "generated_audio"

TEMP_DIR.mkdir(exist_ok=True)
AUDIO_DIR.mkdir(exist_ok=True)

# ================= ROUTES =================

@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/translator")
async def translator(request: Request):
    return templates.TemplateResponse("translator.html", {"request": request})

@app.post("/translate")
async def translate(
    audio: UploadFile = File(...),
    target_language: str = Form(...),
    source_language: str = Form(None)
):
    temp_file = TEMP_DIR / f"{uuid4().hex}.webm"

    try:
        with open(temp_file, "wb") as buffer:
            shutil.copyfileobj(audio.file, buffer)

        result = process_audio(
            str(temp_file),
            target_language,
            source_language
        )

        return JSONResponse(content=result)

    except Exception as e:
        return JSONResponse(
            content={"error": str(e)},
            status_code=500
        )

    finally:
        if temp_file.exists():
            temp_file.unlink()


@app.get("/audio/{filename}")
async def get_audio(filename: str):
    file_path = AUDIO_DIR / filename

    if not file_path.exists() or file_path.suffix.lower() != ".mp3":
        return JSONResponse(
            content={"error": "Audio file not found"},
            status_code=404
        )

    return FileResponse(
        file_path,
        media_type="audio/mpeg",
        filename=filename
    )