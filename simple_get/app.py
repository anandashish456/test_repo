import requests

def call_func():
    response = requests.get("https://www.google.com")
    print(response.status_code)

print("simple")
