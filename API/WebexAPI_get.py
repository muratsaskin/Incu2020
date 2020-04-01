import requests

roomId = 'Y2lzY29zcGFyazovL3VzL1JPT00vYzdhNDUxYTQtZmI1Yi0zNGZlLWIwMTAtZTM0OWJhZjBhYjkx'
token = 'YTc1YmU4MTgtMDM5MS00ZGU2LWFjMGQtMWQwODk3OTYwNWM3MDJiYWNiOWUtYTBl_PF84_consumer'

url = "https://api.ciscospark.com/v1/messages?roomId=" + roomId

header = {"content-type": "application/json; charset=utf-8",
		  "authorization": "Bearer " + token}

response = requests.get(url, headers = header, verify = True)

print(response.json())