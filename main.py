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

def test_Change_Name():

  from urllib import response
  import requests

response = requests.post("https://petstore.swagger.io/v2/pet", json= {
  "id": 999,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "XJ999",
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


def test_find_by_id():
  from urllib import response
  import requests

response = requests.get("https://petstore.swagger.io/v2/pet/999")

print(response.text)

def test_petstore_status_code():

  from urllib import response
  import requests

response = requests.get("https://petstore.swagger.io/v2/pet/999")

print(response.status_code)

if response.status_code == 200:
    print("ok")
else:
    print("Not.ok")


def test_petstore_find_name():
  from urllib import response
  import requests

response = requests.get("https://petstore.swagger.io/v2/pet/999")

print(response.status_code)
