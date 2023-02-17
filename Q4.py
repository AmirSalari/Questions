import requests
import os

URL = "https://f.hubspotusercontent10.net/hubfs/8759415/Major%20U.S.%20Pipline%20Systems%20Shutdown%20After%20Ransomware%20Attack.pdf"
response = requests.get(URL)
open("file.pdf", "wb").write(response.content)

file_size = os.path.getsize("./file.pdf")
print("File Size is :", file_size, "bytes")