# api/utils/scrape_outlets.py
import requests
from bs4 import BeautifulSoup
import sqlite3
import os

URL = "https://zuscoffee.com/category/store/kuala-lumpur-selangor/"
DB_PATH = "api/utils/outlets.db"

def is_valid_outlet(name: str) -> bool:
    name = name.strip().lower()
    return (
        name.startswith("zus coffee") and
        "policy" not in name and
        "kcal" not in name and
        "ingredients" not in name and
        len(name) > 10
    )

def scrape_outlets():
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, "html.parser")
    elements = soup.find_all("p", class_="elementor-heading-title elementor-size-default")

    outlets = []
    for el in elements:
        name = el.get_text(strip=True)
        if name and is_valid_outlet(name):
            outlets.append({
                "name": name,
                "state": "Kuala Lumpur / Selangor",  # Based on page context
                "hours": "N/A",  # Not available directly
                "services": "N/A"  # Not available directly
            })

    return outlets

def save_outlets_to_db(outlets):
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS outlets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            state TEXT,
            hours TEXT,
            services TEXT
        )
    """)
    c.execute("DELETE FROM outlets")  # Clear previous entries
    for outlet in outlets:
        c.execute("""
            INSERT INTO outlets (name, state, hours, services)
            VALUES (?, ?, ?, ?)
        """, (outlet["name"], outlet["state"], outlet["hours"], outlet["services"]))
    conn.commit()
    conn.close()
    print(f"✅ Scraped and saved {len(outlets)} outlets.")

if __name__ == "__main__":
    data = scrape_outlets()
    save_outlets_to_db(data)
