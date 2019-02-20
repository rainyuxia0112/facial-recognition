import requests
from bs4 import BeautifulSoup

# write file
with open ('1.jpg', 'wb') as f:
    res = requests.get('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT94N4UtLSMs0GsGHW3M4xhr2HRCq_xYg2c5B1gYEIx0bC-N-vok92DzA')
    f.write(res.content)

from PIL import Image
Image.open('1.jpg')



#step 1 get the image from website
dataurl = 'https://www.google.com.tw/search?ei=MswPXJnSDMaT8wWwoozQDA&yv=3&q={}&tbm=isch&vet=10ahUKEwiZs6TsgJjfAhXGybwKHTARA8oQuT0IMigB.MswPXJnSDMaT8wWwoozQDA.i&ved=0ahUKEwiZs6TsgJjfAhXGybwKHTARA8oQuT0IMigB&ijn=1&start={}&asearch=ichunk&async=_id:rg_s,_pms:s,_fmt:pc'
import os
os.mkdir('idol_eminem/')
os.mkdir('idol_justin_bieber/')

def getimage(name, dstpath):
    for i in range(3):
        res = requests.get(dataurl.format(name, i * 100))
        soup = BeautifulSoup(res.text, 'lxml')
        for ele in soup.select('img'):
            imgurl = ele.get('src')
            fname  = imgurl.split('tbn:')[1]
            with open(dstpath + fname + '.jpg', 'wb') as f:
                res2 = requests.get(imgurl)
                f.write(res2.content)
getimage('eminem','idol_eminem/')
getimage('justin bieber','idol_justin_bieber/')


# step 2 find face
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


# step 3 build the model, using the Convolution Neural Network
from keras.models import Sequential
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense
classifier = Sequential()
classifier = Sequential()
classifier.add(Conv2D(32, (3, 3), input_shape = (32, 32, 3)))
classifier.add(MaxPooling2D(pool_size = (2, 2)))
classifier.add(Conv2D(32, (3, 3), activation = 'relu'))
classifier.add(MaxPooling2D(pool_size = (2, 2)))
classifier.add(Flatten())
# Fully Connected
classifier.add(Dense(units = 128, activation = 'relu'))
classifier.add(Dense(units = 128, activation = 'relu'))  # second f
classifier.add(Dense(units = 2, activation = 'softmax'))  # finial two label result
classifier.compile(optimizer = 'adam', loss ='categorical_crossentropy', metrics = ['accuracy'])
# import image
from keras.preprocessing.image import ImageDataGenerator
train= ImageDataGenerator(rescale=1/255, shear_range=0.1) #shear_range is moving pictures and generate more pirctures
test= ImageDataGenerator(rescale=1/255)

train_data=train.flow_from_directory('train/',target_size=(32,32),batch_size=10,class_mode='categorical')
test_data=test.flow_from_directory('test/',target_size=(32,32),batch_size=10,class_mode='categorical')

classi=classifier.fit_generator(train_data,nb_enpoch=30, nb_val_samples=10,verbose=1, validation_data=test_data)  #nb_enpoch 迭代，nb_val_samples 10 samples a time