from pathlib import Path
import whisper
from deep_translator import GoogleTranslator
from gtts import gTTS
import time

print("Loading Whisper model...")
model = whisper.load_model("medium")  # change to "small" if needed
print("Model loaded")

AUDIO_DIR = Path("generated_audio")
AUDIO_DIR.mkdir(exist_ok=True)

translation_language_map = {
    "english": "en",
    "hindi": "hi",
    "gujarati": "gu",
    "spanish": "es",
    "french": "fr",
    "german": "de",
    "chinese": "zh-CN",
    "italian": "it",
    "portuguese": "pt",
    "dutch": "nl",
    "russian": "ru",
    "japanese": "ja",
    "arabic": "ar",
    "korean": "ko",
    "turkish": "tr",
    "polish": "pl",
    "vietnamese": "vi",
    "indonesian": "id",
    "thai": "th"
}

tts_language_map = translation_language_map.copy()
whisper_source_map = translation_language_map.copy()
source_translation_map = translation_language_map.copy()


def process_audio(audio_path, target_language, source_language=None):
    try:
        print("Transcribing audio...")

        whisper_language = None
        if source_language:
            whisper_language = whisper_source_map.get(source_language.lower())

        # ✅ FIXED: Force FP32 (no warning)
        result = model.transcribe(
            audio_path,
            language=whisper_language if whisper_language else None,
            fp16=False
        )

        text = result["text"].strip()
        detected_lang = result.get("language", "unknown")

        print("Detected:", detected_lang)
        print("Text:", text)

        if not text:
            return {"error": "Speech not detected. Please speak clearly."}

        target_name = target_language.lower().strip()
        translate_code = translation_language_map.get(target_name)

        if not translate_code:
            return {"error": "Language not supported"}

        source_translate_code = "auto"
        if source_language:
            source_translate_code = source_translation_map.get(
                source_language.lower().strip(),
                "auto"
            )

        # 🌍 Translation
        translated = GoogleTranslator(
            source=source_translate_code,
            target=translate_code
        ).translate(text)

        if not translated:
            return {"error": "Translation failed."}

        print("Translated:", translated)

        audio_url = ""
        tts_code = tts_language_map.get(target_name)

        if tts_code:
            try:
                # ✅ FIXED: unique filename (no overwrite issue)
                filename = f"{time.time_ns()}.mp3"
                speech_file = AUDIO_DIR / filename
            
                tts = gTTS(text=translated, lang=tts_code)
                tts.save(str(speech_file))

                audio_url = f"/audio/{filename}"

            except Exception as tts_error:
                print("TTS error:", tts_error)
                audio_url = ""

        return {
            "source_text": text,
            "translated_text": translated,
            "detected_language": detected_lang,
            "audio_url": audio_url
        }

    except Exception as e:
        return {"error": str(e)}