import json
import os
import requests
from requests.auth import HTTPBasicAuth
import json
import xml.etree.ElementTree as ET
import codecs
import zipfile
import io
from tqdm import tqdm
import sys

file_list_download = sys.argv[1]
user, _, password = sys.argv[2].partition(':')

def download_anno(id_task):

    path = 'https://camera.cvat.bigdataz.dev/api/v1/tasks/{}/annotations?format=CVAT%20for%20images%201.1&filename=doanxem.zip&action=download'.format(id_task)
    username = user
    password = password

    for i in range(10):
        res = requests.get(path, auth=HTTPBasicAuth(username, password))
        if res.status_code == 200:
            content = res.content
            z = zipfile.ZipFile(io.BytesIO(content))
            xml = z.read('annotations.xml')
            z.close()
            return xml
    return None

save_dir = 'download'
if not os.path.isdir(save_dir):
    os.mkdir(save_dir)

with open('lookup_table_name.json') as json_file:
    name_mapping_id = json.load(json_file)

availabel_names = name_mapping_id.keys()

with open(file_list_download, 'r') as f:
    name_list = f.readlines()

tbar = tqdm(name_list)
for name in tbar:
    name = name.strip()
    if name in availabel_names:
        id_task = name_mapping_id[name]
        tbar.set_description('downloading: {} - {}'.format(id_task, name))
        xml = download_anno(id_task)
        if xml is not None:
            with open('{}/{}.xml'.format(save_dir, name), 'wb') as f:
                f.write(xml)
        else:
            print(' >>>>> ERROR: something went wrong with id task: {} | name: {}', id_task, name)
    else:
        print(' >>>>> ERROR: name: "{}" is not available'.format(name))


# python auto_download.py  list_name_download.txt 
