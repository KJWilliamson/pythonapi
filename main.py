import requests
import json

api_url = "https://swapi.dev/api/planets/1/"
# get or post for api requests
# response 200 means success
# when we add .text gives info
planet_response = requests.get(api_url).text
# load s takes strings and makes it dict
planet_response = json.loads(planet_response)
# dumps and indent is pretty print
names = []
for link in planet_response["residents"]:
    people_response = json.loads(requests.get(link).text)
    names.append(people_response["name"])

planet_response["residents"] = names


print(json.dumps(planet_response, indent=4))
