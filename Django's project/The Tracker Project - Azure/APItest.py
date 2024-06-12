

import requests

url = "https://validate-phone-by-api-ninjas.p.rapidapi.com/v1/validatephone"

querystring = {"number":"+16032649267"}

headers = {
	"content-type": "application/octet-stream",
	"X-RapidAPI-Key": "6b6830f7f5msh36a077104b6fdcbp19d6b9jsn4eb36ae47d3f",
	"X-RapidAPI-Host": "validate-phone-by-api-ninjas.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())
d = response.json()

print(d['timezones'][0])