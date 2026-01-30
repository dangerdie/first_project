from dotenv import load_dotenv
import os

def print_author():
    load_dotenv()  # загрузит переменные из .env (если он рядом с main.py)
    author = os.getenv("AUTHOR")
    print(f"Автор проекта: {author}")

print_author()