#!/usr/bin/python3

from PIL import Image
import os

path = './images/'
save_path = '/opt/icons/'

filelist = [s for s in os.listdir(path)]
print(filelist)

for image in filelist:
    if image == '.DS_Store':
        continue
    else:
        im = Image.open(path + image)
        print(im.format, im.size, im.mode)
        resized_im = im.rotate(90).resize((128, 128)).convert('RGB').save(save_path + image, 'JPEG')
