import requests

url = ""
result = requests.get("http://data.fixer.io/api/latest?access_key=3eaf33d4a77e6bd74182ebc4c486ad51")

print(result)

print(result.json())