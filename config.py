from dotenv import load_dotenv
import os

load_dotenv()

USER = os.getenv("USER")
PORT = os.getenv("PORT")
HOST = os.getenv("HOST")
PASSWORD = os.getenv("PASSWORD")
DATABASE = os.getenv("DATABASE")



HF_TOKEN = os.getenv("HF_TOKEN")
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")