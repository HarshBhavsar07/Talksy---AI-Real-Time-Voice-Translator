# 🎙️ Talksy — AI Real-Time Voice Translator

Talksy is a full-stack AI application that converts spoken language into translated speech in real time. It integrates **speech-to-text (Faster-Whisper)**, **translation (Deep Translator)**, and **text-to-speech (gTTS)** into a seamless pipeline powered by **FastAPI** and a browser-based interface.

This guide is intentionally **very detailed and beginner-proof** so that any user can set up and run the project **without errors**.

---

# 🚀 COMPLETE ZERO-ERROR SETUP GUIDE

---

# 🖥️ STEP 1: Install Python (CRITICAL STEP)

### ✔️ Required Version:

* Python **3.9 / 3.10 / 3.11**
* ❌ Avoid Python 3.12 (can break some dependencies)

---

## 🔍 Check if Python is installed

Open terminal (Command Prompt / PowerShell):

```bash
python --version
```

👉 Expected output:

```
Python 3.10.x
```

---

## ❌ If Python is NOT installed:

1. Go to: https://www.python.org/downloads/
2. Download Python **3.10 or 3.11**
3. During installation:

   * ✔️ Tick **“Add Python to PATH”**
   * ✔️ Select **Install for all users (optional)**
4. Click Install

---

## ⚠️ If "python not recognized" error appears:

Restart your system OR reinstall Python properly with PATH enabled.

---

# 📥 STEP 2: Download Project from GitHub

---

## Method 1 (Recommended — Using Git)

```bash
git clone https://github.com/HarshBhavsar07/Talksy---AI-Real-Time-Voice-Translator.git
cd Talksy---AI-Real-Time-Voice-Translator
```

---

## Method 2 (Manual)

1. Click **Code → Download ZIP**
2. Extract folder
3. Open in VS Code

---

# 📁 STEP 3: Open Project in VS Code

1. Open VS Code
2. Click **File → Open Folder**
3. Select your project folder

---

# 🧪 STEP 4: Create Virtual Environment (VERY IMPORTANT)

👉 Prevents dependency conflicts

```bash
python -m venv venv
```

---

# ⚡ STEP 5: Activate Virtual Environment

## Windows:

```bash
venv\Scripts\activate
```

👉 You should see:

```
(venv)
```

---

## Mac/Linux:

```bash
source venv/bin/activate
```

---

## ❌ If activation fails:

Run PowerShell as Administrator:

```bash
Set-ExecutionPolicy RemoteSigned
```

Then retry activation.

---

# 📦 STEP 6: Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔁 If error occurs:

```bash
pip install fastapi uvicorn faster-whisper deep-translator gtts jinja2 python-multipart
```

---

## ⚠️ If pip is outdated:

```bash
python -m pip install --upgrade pip
```

---

# 🤖 STEP 7: AI Model Setup (Automatic)

* No manual download needed
* Faster-Whisper model downloads automatically
* First run takes **1–5 minutes**
* Internet connection required

---

# ▶️ STEP 8: Start Backend Server

```bash
uvicorn app:app --reload
```

---

## ✅ Expected output:

```
Uvicorn running on http://127.0.0.1:8000
```

---

## ⚠️ Important:

* Do NOT close terminal
* Keep server running

---

# 🌐 STEP 9: Open Web Application

Open browser:

```
http://127.0.0.1:8000
```

---

# 🎤 STEP 10: How to Use Application

1. Open website
2. Click **Record / Upload Audio**
3. Speak clearly
4. Select target language
5. Click translate
6. Output will show:

   * Translated text
   * Audio playback

---

# 📁 PROJECT STRUCTURE (EXPLAINED)

```
app.py              → FastAPI backend
final.py            → Core AI pipeline logic
templates/          → HTML frontend
static/
  ├── css/          → Styling
  ├── javascript/   → Frontend logic
  └── image/        → UI assets
requirements.txt    → Dependencies
```

---

# ⚠️ COMMON ERRORS & SOLUTIONS

---

## ❌ ModuleNotFoundError

✔️ Fix:

```
pip install -r requirements.txt
```

---

## ❌ Python not recognized

✔️ Fix:

* Reinstall Python with PATH enabled

---

## ❌ Port already in use

```bash
uvicorn app:app --reload --port 8001
```

---

## ❌ Microphone not working

✔️ Allow mic access in browser
✔️ Use Chrome browser

---

## ❌ Audio not playing

✔️ Check system volume
✔️ Check browser permissions

---

## ❌ Slow first run

✔️ Normal (model downloading)

---

## ❌ Virtual environment not activating

✔️ Run terminal as admin
✔️ Use correct command

---

## ❌ Whisper model errors

✔️ Ensure internet connection
✔️ Restart server

---

# 🧠 IMPORTANT NOTES

* First run is always slow
* Internet required for translation
* Works best in Chrome
* Fully extendable

---

# 🎯 WHAT THIS PROJECT DEMONSTRATES

* AI Speech Recognition
* Language Translation
* Text-to-Speech
* Backend + Frontend Integration
* Real-time processing

---

# 👨‍💻 AUTHOR

Harsh Bhavsar
Computer Engineering

---

# ⭐ SUPPORT

If you liked this project:

* ⭐ Star the repo
* 🍴 Fork it
* 🚀 Improve it

---

> Speak once.
> Let AI carry your voice across languages.
