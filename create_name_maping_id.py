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
from tqdm import tqdm


with open('lookup_table_name.json') as json_file:
    mapping = json.load(json_file)

username = 'moderator'
password = '#Cvat@1920'

for i in tqdm(range(1500)):
    path = 'https://camera.cvat.bigdataz.dev/api/v1/tasks/{}'.format(i)

    res = requests.get(path, auth=HTTPBasicAuth(username, password))

    if res.status_code == 404:
        continue
    else:
        content = res.content.decode('utf-8')
        content_json = json.loads(content)
        name_task = content_json['name']
        mapping[name_task] = i

        with open('lookup_table_name.json', 'w') as outfile:
            json.dump(mapping, outfile, indent=4, sort_keys=True)

    

