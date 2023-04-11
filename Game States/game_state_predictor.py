
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D, MaxPool2D, Flatten

#makes the neural network
model = Sequential()

model.add(Conv2D(filters=128,kernel_size=(4,4),strides=(8,15),padding='valid',input_shape=(32,60,1),activation='relu'))
model.add(MaxPool2D(pool_size=(2,2)))

model.add(Flatten())

model.add(Dense(neurons,activation='relu'))

model.add(Dense(5,activation='softmax'))

model.compile(loss='categorical_crossentropy',optimizer='adam',metrics=['accuracy'])

def predict_state():
