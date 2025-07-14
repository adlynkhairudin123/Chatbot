import requests
from bs4 import BeautifulSoup
import json

URL = "https://shop.zuscoffee.com/collections/drinkware"
HEADERS = {"User-Agent": "Mozilla/5.0"}

def scrape_drinkware():
    response = requests.get(URL, headers=HEADERS)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")

    products = []

    # Loop through product cards
    for product_card in soup.select(".product-card"):
        title_el = product_card.select_one(".product-card__title")
        link_el = product_card.find("a", href=True)

        if not title_el or not link_el:
            continue

        title = title_el.get_text(strip=True)
        link = "https://shop.zuscoffee.com" + link_el["href"]

        # Fetch individual product page to extract description
        try:
            product_page = requests.get(link, headers=HEADERS)
            product_page.raise_for_status()
            product_soup = BeautifulSoup(product_page.text, "html.parser")

            # desc_tag = product_soup.select_one("details.product-info__accordion[open] .accordion__content .prose")
            desc_tag = product_soup.select_one(".accordion__content .prose")
            description = desc_tag.get_text(strip=True) if desc_tag else "No description found"
        except Exception as e:
            description = f"Failed to retrieve description: {e}"

        products.append({
            "title": title,
            "url": link,
            "description": description
        })

    with open("api/utils/products.json", "w", encoding="utf-8") as f:
        json.dump(products, f, ensure_ascii=False, indent=2)

    print(f"✅ Scraped {len(products)} products to products.json")

if __name__ == "__main__":
    scrape_drinkware()
