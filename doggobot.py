import requests
import shutil
import sys

url = "https://dog.ceo/api/breeds/image/random/3"

#print(r.json()['message'])

r = requests.get(url, stream = True)
urls = r.json()['message']
user = sys.argv[1]

for img in urls:
    filename = "/home/"+user+"/dogs/"+'-'.join(img.split('/')[-2:])
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
