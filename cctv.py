import requests

API_KEY = "ADAe5QEn7WHiQFh4qvf3LPI0KCH3UoPH6mYEYyoY8"

url = "https://www.utic.go.kr/main/main.do"

params = {
    "apiKey": API_KEY
}

response = requests.get(url, params=params)

data = response.json()

print(data)