import time, hashlib, os, sys
from urllib.request import urlopen
f = open('info.txt')
lines = f.readlines()
url = lines[1]
response = urlopen(url).read()
currentHash = hashlib.sha224(response).hexdigest()

while True:
    try:
        response = urlopen(url).read()
        currentHash = hashlib.sha224(response).hexdigest()
        time.sleep(10)
        response = urlopen(url).read()
        newHash = hashlib.sha224(response).hexdigest()

        if newHash == currentHash:
            continue

        else:
            os.system('send-mail.py')
            response = urlopen(url).read()
            currentHash = hashlib.sha224(response).hexdigest()
            time.sleep(10)
            continue

    except Exception as e:
        print('an error occured')
