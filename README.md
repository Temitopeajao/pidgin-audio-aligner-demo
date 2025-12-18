# Low-Resource Language Data Pipeline (Nigerian Pidgin)

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Librosa](https://img.shields.io/badge/Audio-Librosa-orange)
![NLP](https://img.shields.io/badge/NLP-Regex-green)

## 📋 Project Overview
This repository contains a **Proof of Concept (PoC)** data engineering pipeline designed to preprocess **low-resource African languages** (specifically Nigerian Pidgin) for Large Language Model (LLM) and Automatic Speech Recognition (ASR) training.

The scripts demonstrated here replicate the **ETL and alignment logic** I engineered during the development of sovereign AI models, addressing specific challenges like code-switching, non-standard orthography, and audio-text alignment.

> **Note:** This is a demonstration repository using open-source logic. It does not contain proprietary data or source code from Awarri AI or the N-ATLAS project.

## ⚡ The Challenge
Standard NLP tools (like default silence detection or English tokenizers) fail when applied to **Nigerian Pidgin** due to:
1.  **Code-Switching Cadence:** Speakers switch rapidly between English and Pidgin, creating "micro-pauses" that standard chunkers mistake for sentence boundaries.
2.  **Noisy Orthography:** Pidgin lacks a standardized spelling system (e.g., *"wetin"* vs *"weytin"*), leading to high token perplexity during model training.

## 🛠️ Key Modules

### 1. Adaptive Audio Chunking (`chunker.py`)
A custom audio segmentation script using `pydub` and `librosa`.
*   **Feature:** Implements an adaptive silence threshold that calculates the ambient noise floor before splitting.
*   **Logic:** specifically tuned to ignore "micro-pauses" (<300ms) typical in West African speech patterns, ensuring that sentences are not cut in the middle of a phrase.

### 2. Pidgin Text Normalization (`normalizer.py`)
A robust text cleaning pipeline designed to standardize crowdsourced transcripts.
*   **Feature:** Regex-based substitution map to handle common spelling variations.
*   **Logic:** Converts unstructured text into a normalized format (removing special characters, standardizing "dey/de", "na/nah") to prepare for Tokenization.

## 📂 Project Structure
```bash
├── audio_processing/
│   ├── chunker.py          # Logic for splitting long-form audio
│   └── silence_detect.py   # Helper utility to find optimal split points
├── text_processing/
│   ├── normalizer.py       # Cleaning script for Pidgin text
│   └── tokenizer_prep.py   # Preparing text for LLM ingestion
├── data/
│   └── sample_audio/       # (Empty placeholder for local testing)
├── requirements.txt
└── README.md
