import json
import requests

url = "https://mp3quran.net/api/v3/suwar"

res = requests.get(url)

api = json.loads(res.text)

# Extract just the names
names = [item['name'] for item in api['suwar']]

# Print the names
for name in names:
    print(name)

    
