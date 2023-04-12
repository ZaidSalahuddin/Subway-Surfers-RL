import pyautogui
import numpy as np
import cv2
import time 

from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import Dense, Conv2D, MaxPool2D, Flatten

#set bounding box for screenshots
bbox = 620,0,650,1200

#set up the neural networks
#function to make models with different number of neurons in the first layer

def make_model(neurons):
    model = Sequential()

    model.add(Conv2D(filters=128,kernel_size=(4,4),strides=(8,15),padding='valid',input_shape=(32,60,1),activation='relu'))
    model.add(MaxPool2D(pool_size=(2,2)))

    model.add(Flatten())

    model.add(Dense(neurons,activation='relu'))

    model.add(Dense(5,activation='softmax'))

    model.compile(loss='categorical_crossentropy',optimizer='adam',metrics=['accuracy'])

    return model 

#makes models and gives the weights
model8 = load_model(r"C:\Users\Zaid Salahuddin\Documents\Snek Schizms\Subway-Surfers-RL\Game States\models\model8")
#model8 = make_model(8)
#model8.load_weights(r'C:\Users\Zaid Salahuddin\Documents\Snek Schizms\Subway-Surfers-RL\Game States\models\model8.data-00000-of-00001')

model32 = make_model(32)
model32.load_weights(r'models\model32.data-00000-of-00001')

model128 = make_model(128)
model128.load_weights(r'models\model128.data-00000-of-00001')

#function to predict from model
def model_predict(model,input):
    predictions = model.predict(input)
    predictions = np.argmax(predictions, axis=1)
    return predictions

#function to proccess the image
def image_process(image):
    image = cv2.resize(image,(32,60)) # resize value could either be (65,120), (32,60) or (22,40). idk if latter gives up too much detail, third is too little detail
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image = image/255
    return image

#main loop
while True:
    # Take a screenshot and process image
    image = pyautogui.screenshot(region=(bbox))
    image = image_process(image)

    #gets preditcitions
    predict8 = model_predict(model8,image)
    predict32 = model_predict(model32,image)
    predict128 = model_predict(model128,image)

    print("8 neurons:",predict8," 32 neurons:", predict32, " 128 neurons:", predict128)
    
    # Wait for 1 seconds
    time.sleep(1)