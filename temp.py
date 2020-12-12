# import urllib.request
# password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
# top_level_url = 'https://camera.cvat.bigdataz.dev/'
# password_mgr.add_password(None, top_level_url, 'moderator', '#Cvat@1920')

# handler = urllib.request.HTTPBasicAuthHandler(password_mgr)

# opener = urllib.request.build_opener(handler)

# opener.open(path)

# urllib.request.urlretrieve(path, 'temp.zip')


import requests
from requests.auth import HTTPBasicAuth
import json
import xml.etree.ElementTree as ET
import codecs
import zipfile
import io



theurl= 'myLink_queriedResult/result.xls'
path = 'https://camera.cvat.bigdataz.dev/api/v1/tasks/142/annotations?format=CVAT%20for%20images%201.1&filename=doanxem.zip&action=download'
# path = 'https://camera.cvat.bigdataz.dev/api/v1/tasks/142'
username = 'moderator'
password = '#Cvat@1920'

while True:
    res = requests.get(path, auth=HTTPBasicAuth(username, password))

    print(res.status_code)
    if res.status_code == 200:

        content = res.content
        print('>> content: ', content[:50])
        z = zipfile.ZipFile(io.BytesIO(content))
        xml = z.read('annotations.xml')
        with open('data.xml', 'wb') as f:
            f.write(xml)
        # print('> xml: ', xml)
        z.extractall()                 # Copies foo.txt to the filesystem

        z.close()

        # content = content.split('')
        # print(content[:50])
        # with open('data.xml', 'wb') as f:
        #     f.write(content)
        break


