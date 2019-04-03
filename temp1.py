'''
import glob 
import cv2
import sys

cascPath = "haarcascade_frontalface_default.xml"

# Create the haar cascade
faceCascade = cv2.CascadeClassifier(cascPath)

while 1 :
#    filename = input("Enter the file name in which images are present = ")
    for img in glob.glob('C:/Users/Dell/Desktop/Random/Random/*.*'):
        try :
            image = cv2.imread(img)
            print("00")
            cv2.imshow(str(img) ,image)
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
            
#            if(len(faces))
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        
        except Exception as e:
            print (e)
    user_input = input("do you want to read another folder = ")
    if user_input == 'no':
        break
'''
#import the library opencv
import cv2
#globbing utility.
import glob
#select the path
#I have provided my path from my local computer, please change it accordingly
path = "C:/Users/Dell/Desktop/Random/Random*.*"
for file in glob.glob(path):
    print(file)
    a= cv2.imread(file)
    print(a)
    #conversion numpy array into rgb image to show
    c = cv2.cvtColor(a, cv2.COLOR_BGR2RGB)
    cv2.imshow('Color image', c)
    #wait for 1 second
    k = cv2.waitKey(1000)
    #destroy the window
    cv2.destroyAllWindows()
