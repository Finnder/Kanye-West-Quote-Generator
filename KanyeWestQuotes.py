import json
import requests

url = 'https://api.kanye.rest/'
requrl = requests.get(url)
jsonparse = requrl.json()


print(" ")
print("'" + jsonparse['quote'] + "'"+ ' - Kanye West')
print(" ")

x = input("Press Enter To Quit")
