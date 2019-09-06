import sys
import cv2 as cv

import os
root_dir = "./cat/"

def detect(imagefilename, cascadefilename):
    err = False
    srcimg = cv.imread(imagefilename)
    if srcimg is None:
        print('cannot load image')
        sys.exit(-1)
    dstimg = srcimg.copy()
    cascade = cv.CascadeClassifier(cascadefilename)
    if cascade.empty():
        print('cannnot load cascade file')
        sys.exit(-1)
    try:
        objects = cascade.detectMultiScale(srcimg, 1.1, 3,minSize=(50,50))
        for (x, y, w, h) in objects:
            print(x, y, w, h)
            cv.rectangle(dstimg, (x, y), (x + w, y + h), (0, 0, 255), 2)
            dstimg = dstimg[y:(y+h),x:(x+w)]
            err = True
    except :
        err = False
    return dstimg,err

if __name__ == '__main__':
    img_list = os.listdir(root_dir)
    for img_name in img_list:
        path = os.path.join(root_dir,img_name)
        print(path)
        result,err = detect(path, 'cascade.xml')
        if err:
            cv.imwrite('./cat_face/'+img_name, result)
        else:
            print("err")
