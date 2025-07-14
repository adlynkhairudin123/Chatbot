import requests

# Test /products endpoint
product_query = "Do you have a ZUS tumbler?"
product_res = requests.get("http://127.0.0.1:8000/api/products", params={"query": product_query})
print("🔍 /products response:")
print(product_res.json())

# Test /outlets endpoint
outlet_query = "List all outlets in Selangor"
outlet_res = requests.get("http://127.0.0.1:8000/api/outlets", params={"query": outlet_query})
print("\n🏬 /outlets response:")
print(outlet_res.json())

# Failure test - products
bad_product_query = ""
bad_product_res = requests.get("http://127.0.0.1:8000/api/products", params={"query": bad_product_query})
print("\n❌ /products failure:")
print(bad_product_res.json())

# Failure test - outlets
bad_outlet_query = "How many outlets are on the moon?"
bad_outlet_res = requests.get("http://127.0.0.1:8000/api/outlets", params={"query": bad_outlet_query})
print("\n❌ /outlets failure:")
print(bad_outlet_res.json())

# run_test("/products", "please crash", "💥 Simulated crash")

