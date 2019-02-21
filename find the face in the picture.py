# entract face in the picture
from PIL import Image
import cv2 as cv
face_cascade = cv.CascadeClassifier('/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/cv2/data/haarcascade_frontalface_default.xml')
img = cv.imread('/Users/rain/Desktop/people.jpg')
faces = face_cascade.detectMultiScale(img, 1.2, 3)
from PIL import Image
im = Image.open('/Users/rain/Desktop/people.jpg')

from matplotlib import pyplot as plt
font = cv.FONT_HERSHEY_PLAIN
for x,y,w,h in faces:
    box = (x, y, x+w, y+h)
    crpim = im.crop(box).resize((32,32))
    cv.rectangle(img,(x,y),(x+w,y+h),(14,180,255),2)
plt.figure(figsize=(30,20))
plt.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB))