import requests

BASE_URL = "http://127.0.0.1:8000/api"

def test_missing_products_query():
    print("❌ /products missing query:")
    res = requests.get(f"{BASE_URL}/products", params={"query": ""})
    print(res.json())

def test_missing_outlets_query():
    print("\n❌ /outlets missing query:")
    res = requests.get(f"{BASE_URL}/outlets", params={"query": ""})
    print(res.json())

def test_simulated_crash():
    print("\n Simulated crash test:")
    res = requests.get(f"{BASE_URL}/products", params={"query": "please crash"})
    print(res.json())

def test_sql_injection():
    print("\n SQL injection attempt:")
    payload = "' OR 1=1 --"
    res = requests.get(f"{BASE_URL}/outlets", params={"query": payload})
    print(res.json())

if __name__ == "__main__":
    test_missing_products_query()
    test_missing_outlets_query()
    test_simulated_crash()
    test_sql_injection()
