os.mkdir('idol_eminem_final/')
import os
for ele in os.listdir('idol_eminem/')[1:]:
    import cv2 as cv
    from PIL import Image
    img = Image.open('idol_eminem/' + ele)
    img_re = cv.imread('idol_eminem/' +ele)
    face_cascade = cv.CascadeClassifier('/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/cv2/data/haarcascade_frontalface_default.xml')
    face = face_cascade.detectMultiScale(img_re, 1.3, 5)
    if len(face)==1:
        x, y, w, h = face[0]
        crpim = img.crop((x, y, x + w, y + h)).resize((32, 32))
        crpim.save('idol_eminem_final/'+ ele)


os.mkdir('idol_justin_bieber_final/')
import os
for ele in os.listdir('idol_justin_bieber/')[1:]:
    import cv2 as cv
    from PIL import Image
    img = Image.open('idol_justin_bieber/' + ele)
    img_re = cv.imread('idol_justin_bieber/' +ele)
    face_cascade = cv.CascadeClassifier('/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/cv2/data/haarcascade_frontalface_default.xml')
    face = face_cascade.detectMultiScale(img_re, 1.3, 5)
    if len(face)==1:
        x, y, w, h = face[0]
        crpim = img.crop((x, y, x + w, y + h)).resize((32, 32))
        crpim.save('idol_justin_bieber_final/'+ ele)