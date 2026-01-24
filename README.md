# 🎙️ Pidgin Audio Aligner & Segmenter  
## Ground-Truth Dataset Builder for Nigerian Pidgin ASR

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![ASR](https://img.shields.io/badge/Focus-Speech%20Recognition-red)
![Audio](https://img.shields.io/badge/Audio-Processing-orange)
![Dataset](https://img.shields.io/badge/Output-JSONL-green)
![License](https://img.shields.io/badge/License-MIT-lightgrey)
![Status](https://img.shields.io/badge/Status-Active-success)

> A lightweight pipeline for cleaning, validating, and segmenting Nigerian Pidgin audio into model-ready ASR training manifests.

---

## 📋 Overview

The **Pidgin Audio Aligner & Segmenter** prepares high-quality **ground-truth datasets** for Automatic Speech Recognition (ASR) systems such as:

- OpenAI Whisper  
- Wav2Vec2  
- NVIDIA NeMo  
- Hugging Face speech models  

Raw transcripts typically contain:

- Long clips that cause GPU memory issues  
- Silence or background noise  
- Incorrect timestamps  
- Poor segmentation  

These problems significantly degrade ASR performance.

This tool automatically **filters, validates, and formats audio segments** into a clean `manifest.jsonl` ready for training.

---

## ✨ Features

### ⏱️ Duration Filtering
Removes clips:
- < 1s → likely noise  
- > 30s → GPU out-of-memory risk  

### 🔇 Silence & Noise Removal
Drops segments labeled:
- `[silence]`
- `[noise]`
- `[music]`

### 🧮 Timestamp Validation
Ensures:
- Correct start/end offsets
- No overlaps
- Accurate durations

### 📦 JSONL Manifest Generation
Outputs training-ready format compatible with:
- NVIDIA NeMo
- Hugging Face
- Whisper fine-tuning

### ⚡ Lightweight
Pure Python pipeline with minimal dependencies.

---

## 🛠️ Why This Matters

### The Problem
Speech datasets for low-resource languages are messy.

Messy audio → poor alignments → bad ASR models.

### The Fix
Clean segmentation → stable training → higher WER accuracy.

### The Result
✔ Better transcripts  
✔ Faster training  
✔ Fewer OOM crashes  
✔ Higher ASR performance  

---

## 🧱 Architecture

```
Raw Audio + Transcript
        │
        ▼
Timestamp Validation
        │
        ▼
Duration Filtering
        │
        ▼
Silence / Noise Removal
        │
        ▼
Segment Extraction
        │
        ▼
manifest.jsonl (training-ready)
        │
        ▼
ASR Model Training (Whisper / NeMo / Wav2Vec)
```

---

## ⚙️ Installation

### Clone repository

```bash
git clone https://github.com/yourusername/pidgin-audio-aligner.git
cd pidgin-audio-aligner
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

### Run demo

```bash
python audio_aligner.py
```

---

## 🧪 Example Output (manifest.jsonl)

Each line:

```json
{"audio_filepath": "clips/001.wav", "duration": 4.32, "text": "how you dey today"}
{"audio_filepath": "clips/002.wav", "duration": 2.91, "text": "i dey fine"}
```

Directly usable for:
- NeMo
- HuggingFace
- Whisper training scripts

---

## 🧰 Built With

- Python
- JSONL formatting
- Audio preprocessing techniques
- ASR dataset engineering
- Timestamp alignment logic

---

## 📂 Project Structure

```
pidgin-audio-aligner/
│
├── audio_aligner.py     # Core alignment pipeline
├── filters.py           # Duration & noise filters
├── utils.py             # Helper functions
├── data/                # Sample transcripts/audio
├── output/              # Generated manifests
├── requirements.txt
└── README.md
```

---
## 🧪 Example Use Cases

- Whisper fine-tuning
- NeMo ASR training
- Speech corpus cleaning
- Podcast segmentation
- Low-resource speech research
- African language ASR systems

---

## 🔬 Roadmap

- [ ] Automatic silence detection (VAD)
- [ ] Batch directory processing
- [ ] CLI tool
- [ ] Web dashboard
- [ ] HuggingFace dataset export
- [ ] Multi-language support (Yoruba/Hausa/Igbo)
- [ ] Speaker diarization support

---

## 🤝 Contributing

Contributions welcome.

Ideas:
- Better segmentation logic
- Voice activity detection
- Performance improvements
- Dataset benchmarks

Open an issue or PR anytime.

---

## 👤 Author

**Temitope Ajao**  
AI Engineer & LLM Specialist  

[LinkedIn](www.linkedin.com/in/temitope-ajao-4a8670302) • [Email](mailto:topekele@gmail.com)

---

## 📜 License

MIT License

---

## ⭐ If this project helps you
Give it a star — it supports African Speech AI research ✨
