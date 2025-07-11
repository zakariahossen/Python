import requests
import time

url = "example.com"  # 🔁 Replace with your target URL

# you can use a infinite loop (While True) instead of for loop.
for i in range(50):
    try:
        response = requests.get(url)
        print(f"Visit {i+1}: Status Code = {response.status_code}")
        time.sleep(1)  # 💤 Delay to avoid hammering the server too hard
    except requests.exceptions.RequestException as e:
        print(f"Visit {i+1}: Failed - {e}")
