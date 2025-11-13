# src/fetch_sj.py
import os
import time
import json
import requests
from datetime import datetime
from typing import List, Dict

SJ_BASE_URL = "https://api.superjob.ru/2.0"
RAW_DIR = "data/raw"
SJ_API_KEY = os.getenv("SJ_API_KEY")  # ОБЯЗАТЕЛЬНО установи!

HEADERS = {
    "X-Api-App-Id": SJ_API_KEY if SJ_API_KEY else "",
    "User-Agent": "RH-AI-Memory-Agent/1.0",
}

def _ensure_key():
    if not SJ_API_KEY:
        raise RuntimeError("Не установлен переменная окружения SJ_API_KEY")

def fetch_sj_vacancies(keyword: str, pages: int=5) -> List[Dict]:
    _ensure_key()
    all_items = []
    page = 0
    while page < pages:
        params = {"keyword": keyword, "page": page, "count": 100}
        resp = requests.get(f"{SJ_BASE_URL}/vacancies/", params=params, headers=HEADERS, timeout=20)
        if resp.status_code == 429:
            print("[RATE] SJ 429 Too Many Requests — спим 2 сек")
            time.sleep(2)
            continue
        resp.raise_for_status()
        data = resp.json()
        objs = data.get("objects", [])
        print(f"[SJ] '{keyword}' страница {page+1} — получено {len(objs)}")
        all_items.extend(objs)
        page += 1
        if not data.get("more"):
            break
        time.sleep(0.5)
    return all_items

def collect_sj_batch(queries: List[str], pages:int=5):
    _ensure_key()
    os.makedirs(RAW_DIR, exist_ok=True)
    date_tag = datetime.utcnow().strftime("%Y-%m-%d")
    ndjson_path = os.path.join(RAW_DIR, f"sj_{date_tag}.ndjson")

    total = 0
    with open(ndjson_path, "a", encoding="utf-8") as out:
        for q in queries:
            items = fetch_sj_vacancies(q, pages=pages)
            print(f"[SJ] Найдено {len(items)} коротких карточек по запросу '{q}'")
            for idx, it in enumerate(items, start=1):
                it["_source"] = "sj"
                it["_fetched_at"] = datetime.utcnow().isoformat()
                title = it.get("profession")
                print(f"  → SJ {q}: {idx}/{len(items)} id={it.get('id')} | {title}")
                out.write(json.dumps(it, ensure_ascii=False) + "\n")
                total += 1
                time.sleep(0.2)

    print(f"[OK][SJ] Сохранено {total} вакансий в {ndjson_path}")
    return ndjson_path

if __name__ == "__main__":
    DEFAULT_PROF_AREAS = ["python", "data scientist", "ml engineer", "backend", "education", "edtech"]
    collect_sj_batch(DEFAULT_PROF_AREAS, pages=3)
