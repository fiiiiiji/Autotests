from urllib import response
import requests

response = requests.post("https://petstore.swagger.io/v2/pet", json= {
  "id": 999,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "XJ9",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
})
print(response.text)
