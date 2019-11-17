import json
import requests

url = 'https://api.kanye.rest/'
requrl = requests.get(url)
jsonparse = requrl.json()


print("'" + jsonparse['quote'] + "'"+ ' - Kanye West')
