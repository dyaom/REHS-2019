import tensorflow as tf
from tensorflow import keras
import random
import pandas as pd

TEST_DATA_SIZE = 100000

input('start')

#generate a dataset
rawData = {}
for i in range(TEST_DATA_SIZE):
    rawData[i] = [i%3 == 0, i%5 == 0]
print('generated dataset')

#format as dataframe
data = pd.DataFrame(data=rawData).transpose().set_axis(['f','b'],axis=1,inplace=False)
#split into training/test
testData = data.sample(frac=0.2).sort_index()
trainData = data.drop(testData.index,axis=0)
print('generated dataframe')

#build model
model = keras.Sequential([
    keras.layers.Dense(64, activation=tf.nn.relu, input_shape=[1,]),
    keras.layers.Dense(64, activation=tf.nn.relu),
    keras.layers.Dense(2)])
optimizer = keras.optimizers.RMSprop(0.001)

model.compile(loss='mean_squared_error',
    optimizer=optimizer,
    metrics=['mean_absolute_error', 'mean_squared_error'])

#train model
EPOCHS = 1000
history = model.fit(trainData.index.values, trainData, epochs=EPOCHS,
                    validation_split=0.2, verbose=0)

#test model
loss, mae, mse = model.evaluate(testData.index.values, testData, verbose=0)
print(mae)

print('done')
