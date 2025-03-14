import requests
import os

def download_photo(photo_url):
    response = requests.get(photo_url)

    if response.status_code == 200:
        with open('photo.jpg', 'wb') as f:
            f.write(response.content)
            print("downloaded")
    else:
        print("error downloading")


def delete_photo():
    os.remove('photo.jpg')
    print("deleted")