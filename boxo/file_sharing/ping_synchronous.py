import requests

def ping():
	return requests.get("https://google.com")

print(ping())