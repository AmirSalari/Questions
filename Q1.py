# import requests module
import requests
  
# Making a get request
response = requests.get('https://fortressinfosec.com/')
# print header field of response
print("X-HS-Cache-Config: ", response.headers['X-HS-Cache-Config'])
