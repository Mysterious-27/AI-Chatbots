# 🧑‍💻 AI Excel Mock Interviewer 
## Link for the app - [Click Here](https://ai-chatview.streamlit.app/)

This project is a Streamlit-based web application that simulates a mock Excel interview, allowing candidates to answer real-world Excel questions and receive **automated feedback and scoring** from an AI assistant.

It supports:
- ✅ Google Gemini API (cloud-based evaluation)
- ✅ Ollama (offline/local open-source LLMs like Mistral, LLaMA2)

---

## Features

- Presents Excel-related interview questions.
- Allows users to submit their answers.
- Uses the Gemini API to evaluate answers and provide feedback.
- Displays interview results upon completion.

---

## File Structure

- `app.py`: The Streamlit application code using the Google Gemini API for evaluation.
- `app_ollama.py`: An alternative Streamlit application using an offline Ollama model for evaluation.
- `requirements.txt`: Lists all necessary Python dependencies for both versions.
- `README.md`: This file, providing an overview and setup instructions.



---

## Setup

1.  **Clone the repository (or have the `app.py` file and notebook)**: Ensure you have the `app.py` file containing the Streamlit application code.
2.  **Set up Google Colab**: Open the provided Colab notebook.
3.  **Install dependencies**: Run the cell that installs `streamlit` and `pyngrok`.

Clone this repository or download the files:

```bash
git clone https://github.com/your-username/ai-excel-interviewer.git
cd ai-excel-interviewer
```


## ✅ Option 1: Run with Google Gemini API

Best for cloud use (e.g. Google Colab or Streamlit Cloud)

1. Install dependencies
```bash
pip install streamlit google-generativeai
```
2. Set your api key
```bash

# Linux/macOS
export GOOGLE_API_KEY="your-api-key"

# Windows (CMD)
set GOOGLE_API_KEY=your-api-key
```
## 📦 Requirements

- Python 3.8+
- [Streamlit](https://streamlit.io/)
- [Google Generative AI SDK](https://pypi.org/project/google-generativeai/) *(for Gemini version)*
- [Ollama](https://ollama.com) *(for offline version)*
- `requests`, `pandas` *(for Ollama version)*
## ✅ Option 2: Run Locally with Ollama (Offline) — `app_ollama.py`

Runs entirely on your machine using open-source models like `mistral`.
File included as `app_ollama.py`
