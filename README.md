# Intelligent Plagiarism Detection System

An intelligent system for detecting textual similarity and potential plagiarism using Natural Language Processing (NLP) techniques.

This project allows users to compare a reference text with multiple suspicious texts and receive detailed analytical results including similarity scores, highlighted overlaps, visual charts, and relationship graphs between documents.

## Features

- Compare one reference text with multiple suspicious texts
- Upload or paste texts directly
- Automatic similarity calculation using **TF‑IDF** and **Cosine Similarity**
- Highlight similar phrases between documents
- Visual analytics including **Radar Charts**
- Graph visualization of document relationships
- Downloadable **PDF report**
- Clean and interactive web interface

## Tech Stack

Backend
- Python
- FastAPI
- Scikit‑learn
- Uvicorn

Frontend
- HTML
- CSS
- JavaScript
- Chart.js

Algorithms
- TF‑IDF Vectorization
- Cosine Similarity
- Text preprocessing and normalization

## Project Structure

```
PlagiarismDetector
│
├── backend
│   └── app.py
│
├── frontend
│   └── index.html
│
├── uploads
│
└── requirements.txt
```

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/plagiarism-detector.git
cd plagiarism-detector
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the environment:

Windows
```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install fastapi uvicorn scikit-learn python-multipart
```

Run the server:

```bash
uvicorn backend.app:app --reload
```

Open in browser:

```
http://127.0.0.1:8000
```

## Use Cases

- Academic plagiarism detection
- Research similarity analysis
- Content originality checking
- Educational tools for writing integrity

## Future Improvements

- Support for large document comparison
- AI‑based paraphrase detection
- Multi‑language support
- Database integration

## 🧑🏻‍💻 Authors

- Armin Abdollahi
- Sarina Kasaiyan
