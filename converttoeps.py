import cv2
import os,os.path
from PIL import Image
imageDir = "C:/Users/arjun/Desktop/directory" #specify your path here
image_path_list = []
valid_image_extensions = [".jpg",'.png'] #specify your vald extensions here
valid_image_extensions = [item.lower() for item in valid_image_extensions]
i=0
for file in os.listdir(imageDir):
    i+=1
    extension = os.path.splitext(file)[1]
    if extension.lower() in valid_image_extensions:
        im = Image.open(os.path.join(imageDir, file))
        path=os.path.join(imageDir, file)
        print(file)
        base = os.path.splitext(file)[0]
        print(im.mode)
        if im.mode=='RGBA':
            fig=im.convert('RGB')
        else:
            fig=im
        filename='C:/Users/arjun/Desktop/directory/'+str(base)+'.eps'
        fig.save(filename,lossless=False)
