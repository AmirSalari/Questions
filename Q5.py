import requests
import os

url = "https://f.hubspotusercontent10.net/hubfs/8759415/Major%20U.S.%20Pipline%20Systems%20Shutdown%20After%20Ransomware%20Attack.pdf"
try:
    response = requests.get(url)
    try:
        with open("file.pdf","wb") as f:
            f.write(response.content)
    except IOError:
        print("Something went wrong in working with file:", e)

except Exception as e:
    print("Something went wrong in downloading:", e)

file_size = os.path.getsize("./file.pdf")
print("File Size is :", file_size, "bytes")