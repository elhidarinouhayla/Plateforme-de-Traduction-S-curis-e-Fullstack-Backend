from dotenv import load_dotenv
import os

load_dotenv()

USER = os.getenv("USER")
PORT = os.getenv("PORT", "5432")
HOST = os.getenv("HOST","db")
PASSWORD = os.getenv("PASSWORD", "123")
DATABASE = os.getenv("DATABASE")



HF_TOKEN = os.getenv("HF_TOKEN")
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")