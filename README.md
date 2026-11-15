# Smart FAQ Chatbot

## Project Description
Smart FAQ Chatbot is an AI-powered chatbot that answers questions related to a given syllabus. It uses Ollama and the Llama 3.2 language model to generate answers based on the provided syllabus content.

The application provides a simple interactive interface built using Streamlit.

## Features
- Answers questions about syllabus topics.
- Uses a locally running AI model through Ollama.
- Provides answers based on the supplied syllabus.
- Responds when requested information is not available in the syllabus.
- Simple chat interface using Streamlit.
- Clear chat functionality.

## Technologies Used
- Python
- Streamlit
- Ollama
- Llama 3.2
- Requests

## Project Structure

```text
Smart_FAQ_Chatbot/
│
├── app.py
├── chatbot.py
├── syllabus.txt
├── README.md
├── .gitignore
└── venv/
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/Amritha1806/Smart_FAQ_chatbot.git
```

### 2. Navigate to the project folder

```bash
cd Smart_FAQ_chatbot
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```bash
pip install streamlit requests
```

### 6. Install and start Ollama

Download Ollama from https://ollama.com/

Pull the Llama 3.2 model:

```bash
ollama pull llama3.2
```

### 7. Run the application

```bash
streamlit run app.py
```

The application will open in your browser, usually at:

`http://localhost:8501`

## Future Improvements
- Support PDF syllabus uploads.
- Implement document embeddings and vector search.
- Integrate a Retrieval-Augmented Generation (RAG) pipeline.
- Support multiple syllabus documents.
- Display source references for generated answers.

## Author
Amritha Lakshmi

## Note
This project currently uses the syllabus text provided in `syllabus.txt` as context for generating answers. It is not yet a full RAG implementation.
