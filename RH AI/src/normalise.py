# src/normalize.py
import re
from bs4 import BeautifulSoup

def html_to_text(s: str) -> str:
    if not s:
        return ""
    return BeautifulSoup(s, "html.parser").get_text(" ", strip=True)

def normalize_hh(item: dict) -> dict:
    return {
        "id": f"hh:{item['id']}",
        "source": "hh",
        "title": item.get("name"),
        "employer": (item.get("employer") or {}).get("name"),
        "area": (item.get("area") or {}).get("name"),
        "industry": None,  # можно определить позже по ключевым словам
        "published_at": item.get("published_at"),
        "url": item.get("alternate_url"),
        "description_raw": item.get("description"),
        "description_text": html_to_text(item.get("description", "")),
        "requirements_raw": "",  # можно вытаскивать из description_regexp
        "salary_from": (item.get("salary") or {}).get("from"),
        "salary_to": (item.get("salary") or {}).get("to"),
        "currency": (item.get("salary") or {}).get("currency"),
        "experience": (item.get("experience") or {}).get("name"),
        "employment": (item.get("employment") or {}).get("name"),
        "schedule": (item.get("schedule") or {}).get("name"),
        "skills_extracted": [],
        "skill_groups": {},
        "meta": {
            "api_loaded_at": item.get("_fetched_at"),
            "source_payload": {},
        }
    }

def normalize_sj(item: dict) -> dict:
    return {
        "id": f"sj:{item['id']}",
        "source": "sj",
        "title": item.get("profession"),
        "employer": (item.get("client") or {}).get("title"),
        "area": item.get("town", {}).get("title"),
        "industry": None,
        "published_at": item.get("date_published"),
        "url": item.get("link"),
        "description_raw": item.get("candidat"),
        "description_text": item.get("candidat"),
        "requirements_raw": item.get("candidat"),
        "salary_from": item.get("payment_from"),
        "salary_to": item.get("payment_to"),
        "currency": item.get("currency"),
        "experience": None,
        "employment": None,
        "schedule": None,
        "skills_extracted": [],
        "skill_groups": {},
        "meta": {
            "api_loaded_at": item.get("_fetched_at"),
            "source_payload": {},
        }
    }
