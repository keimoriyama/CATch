from PIL import Image
import os

img_names = os.listdir("./cat_face")
print(img_names)
for names in img_names:
    print(names)

    img = Image.open("./cat_face/"+names)
    size = 128

    img = img.resize((size,size))
    img.save("./cat_face_data/"+names)
