# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 20:54:15 2019

@author: Dell
"""

import cv2
import os, os.path
 
#debug info OpenCV version
print ("OpenCV version: " + cv2.__version__)
 
#image path and valid extensions
imageDir = "C:/Users/Dell/Desktop/Random/Random/" #specify your path here
image_path_list = []
valid_image_extensions = [".jpg", ".jpeg", ".png"] #specify your vald extensions here
valid_image_extensions = [item.lower() for item in valid_image_extensions]
 
#create a list all files in directory and
#append files with a vaild extention to image_path_list
for file in os.listdir(imageDir):
    extension = os.path.splitext(file)[1]
    if extension.lower() not in valid_image_extensions:
        continue
    image_path_list.append(os.path.join(imageDir, file))
i=0
#loop through image_path_list to open each image
for imagePath in image_path_list:
    image = cv2.imread(imagePath)
    
    # display the image on screen with imshow()
    # after checking that it loaded
    if image is not None:
        cv2.imshow(imagePath, image)
        path1 = 'C:/Users/Dell/Desktop/Random/Random/XY/'
        cv2.imwrite(os.path.join(path1 , 'waka.jpg'), image)
        cv2.imwrite(os.path.join(path1 , 'pic{:>05}.jpg'.format(i)), image) 
#        cv2.SaveImage('pic{:>05}.jpg'.format(i), img)
        i+=1
    elif image is None:
        print ("Error loading: " + imagePath)
        #end this loop iteration and move on to next image
        continue
    
    # wait time in milliseconds
    # this is required to show the image
    # 0 = wait indefinitely
    # exit when escape key is pressed
    key = cv2.waitKey(0)
    if key == 27: # escape
        break
 
# close any open windows
cv2.destroyAllWindows()