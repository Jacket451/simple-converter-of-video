# 🎬 Video Converter (Tkinter + FFmpeg)

A simple GUI application written in Python for converting video files into different formats using FFmpeg.

## 📌 Features
  - Select input video file via GUI
  - Supported formats:
     - MP4
     - AVI
     - MKV
     - MOV 
  - Choose output format and file location
  - One-click conversion
  - User-friendly interface built with Tkinter
## 🖥️ Interface
  - Input file selection field
  - Format dropdown menu
  - Output file path field
  - Convert button
## ⚙️ Requirements
  - Python 3.x
  - FFmpeg (required)
## 📥 Installation
1. Install FFmpeg

Download from the official website:
### https://ffmpeg.org/download.html

Add ffmpeg.exe to your system PATH
or place it in the same folder as the executable.

## Install dependencies (if needed)
 ```
 pip install tkinter
 ```
⚠️ Tkinter is usually included with Python by default

## ▶️ Run
```python
python converter.py
```

## 📦 Build .exe (optional)

To create a standalone executable:
```python
pip install pyinstaller
pyinstaller --onefile --windowed --add-binary "ffmpeg.exe;." converter.py
```

The executable will be available in:
dist/converter.exe

## 🧠 How it works

The program uses Python’s subprocess module to run FFmpeg commands.

Different codecs are applied depending on the selected format:
| Format | Video Codec | Audio Codec |
|--------|------------|------------|
| mp4    | libx264    | aac        |
| avi    | mpeg4      | default    |
| mkv    | libx264    | default    |
| mov    | libx264    | aac        |

## ⚠️ Possible Issues
- ❌ ffmpeg.exe not found
→ Make sure FFmpeg is in the same folder or added to PATH
- ❌ No file selected
→ You must choose both input and output files

## 📁 Project Structure
```
project/
│
├── converter.py
├── ffmpeg.exe (optional)
```
