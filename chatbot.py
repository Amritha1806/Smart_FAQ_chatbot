
import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3.2"


def load_syllabus():
    with open("syllabus.txt", "r", encoding="utf-8") as file:
        return file.read()


def get_answer(question):
    syllabus = load_syllabus()

    prompt = f"""
    You are a helpful college syllabus FAQ chatbot.

    Answer the student's question using only the syllabus
    information provided below.

    If the answer is not available in the syllabus,
    clearly say that the information is not available.

    SYLLABUS:
    {syllabus}

    STUDENT QUESTION:
    {question}

    ANSWER:
    """

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL_NAME,
            "prompt": prompt,
            "stream": False
        },
        timeout=180
    )

    response.raise_for_status()

    return response.json()["response"].strip()


if __name__ == "__main__":
    print("===== SMART FAQ CHATBOT =====")

    while True:
        question = input("\nAsk a question (or type exit): ")

        if question.lower() == "exit":
            print("Chatbot closed.")
            break

        answer = get_answer(question)
        print("\nChatbot:", answer)
