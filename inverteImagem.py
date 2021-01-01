from PIL import Image
import PIL.ImageOps
import os

os.makedirs(os.getcwd() + "/imprimir")

for img in os.listdir():
    if ".png" in img:
        image = Image.open(img)
        inverted_image = PIL.ImageOps.invert(image)
        inverted_image.save(os.getcwd()+"/imprimir/new"+img)