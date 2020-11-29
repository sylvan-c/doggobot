import requests
import json
import random
import shutil
import sys

r=requests.get("https://reddit.com/r/dogpictures.json", headers = {'User-agent': 'doggobot'})
#print(r)
out = r.json()

urls = []

while True:
    url = out['data']['children'][random.choice(range(2, 20))]['data']['url']
    if "/gallery/" not in url and url not in urls:
        urls.append(url)
    if len(urls) == 3:
        break

print(urls)

for img in urls:
    user = sys.argv[1]
    filename = "/home/"+user+"/doggobot/"+img.split('/')[-1]
    r = requests.get(img, stream = True)

    ## Check if the media was retrieved successfully
    if r.status_code == 200:
        ## Set decode_content value to True, otherwise the downloaded image file's size will be zero.
        r.raw.decode_content = True
    
        ## Open a local file with wb ( write binary ) permission.
        with open(filename,'wb') as f:
            shutil.copyfileobj(r.raw, f)
        
        print('Successfully downloaded: ',filename)
    else:
        print('Couldn\'t be retrieved')
