from urllib import request
import sys
import os
from PIL import Image
import glob


# see http://image-net.org/archive/words.txt
classes = {"cat":"n02121808"}

offset = 0
max = 10000

def download(url,decode=False):
    response = request.urlopen(url)
    if response.geturl() == "https://s.yimg.com/pw/images/en-us/photo_unavailable.png":
        # Flickr :This photo is no longer available iamge.
        raise Exception("This photo is no longer available iamge.")
    
    body = response.read()
    if decode ==True:
        body = body.decode()
    return body

def write(path,img):
    file = open(path,'wb')
    file.write(img)
    file.close()


def download_cat_image():
    for dir, id in classes.items():
        err = 0
        os.makedirs(dir, exist_ok = True)
        urls = download("http://www.image-net.org/api/text/imagenet.synset.geturls?wnid="+id, decode=True).split()
        i = 0
        for url in urls:
            if i < offset:
                continue
            if i > max:
                break
            try:
                file = os.path.split(url)[1]
                path = dir + "/" + file
                write(path, download(url))
            except:
                err = err + 1
            i = i + 1
    print(err)

def rename():
    path = './cat/*.jpg'
    i = 1

    flist = glob.glob(path)
    for file in flist:
        os.rename(file, "./cat/cat-" + str(i) + '.jpg')
        i += 1
        
if __name__ == "__main__":
    print("-----downloading-------")
    #download_cat_image()
    print("-----renaming-------")
    rename()
