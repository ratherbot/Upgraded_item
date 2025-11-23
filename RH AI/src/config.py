# src/config.py
import os
from dotenv import load_dotenv
load_dotenv()  # подхватит .env из корня проекта

HH_BASE_URL = "https://api.hh.ru"
SJ_BASE_URL = "https://api.superjob.ru/2.0"

# что качаем
DEFAULT_PROF_AREAS = [
    "data scientist", "data analyst", "ml engineer",
    "backend", "python", "ai", "education", "edtech",
]

# ключ SJ из переменных окружения
SJ_API_KEY = os.getenv("SJ_API_KEY", "YOUR_TOKEN_HERE")

# куда сохраняем
DATA_DIR = "data"
RAW_DIR = "data/raw"
PROCESSED_DIR = "data/processed"
