
# import requests module
import requests
  
# Making a get request
response = requests.get('https://fortressinfosec.com/')
# print headers of response
print("X-HS-Cache-Config: ", response.headers['X-HS-Cache-Config'])
