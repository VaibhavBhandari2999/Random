import cv2
import sys
import os

# Get user supplied value
cascPath = "haarcascade_frontalface_default.xml"

# Create the haar cascade
faceCascade = cv2.CascadeClassifier(cascPath)

# Read the image
import glob

images = [cv2.imread(file) for file in glob.glob("D:/Photos from Phone/*.jpg")]
for image in images:
    image = cv2.imread(image)
#image = cv2.imread("trial.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30),
    flags = cv2.CASCADE_SCALE_IMAGE
)
print(len(faces))
path="D:/Photos from Phone/Classified"

if(len(faces)>0):
    cv2.imwrite(os.path.join(path , 'waka.jpg'), imag)
    
print("Found {0} faces!".format(len(faces)))

# Draw a rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv2.imshow("Faces found", image)
cv2.waitKey(0)
