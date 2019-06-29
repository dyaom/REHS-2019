import tensorflow as tf
from tensorflow import keras
import random
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

TEST_DATA_SIZE = 1000
EPOCHS = 250

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

#build f-model
modelF = keras.Sequential([
    keras.layers.Dense(64, activation=tf.nn.relu, input_shape=[1,]),
    keras.layers.Dense(64, activation=tf.nn.relu),
    keras.layers.Dense(1)])
optimizer = keras.optimizers.RMSprop(0.001)

modelF.compile(loss='mean_squared_error',
    optimizer=optimizer,
    metrics=['mean_absolute_error', 'mean_squared_error'])

#build b-model
modelB = keras.Sequential([
    keras.layers.Dense(64, activation=tf.nn.relu, input_shape=[1,]),
    keras.layers.Dense(64, activation=tf.nn.relu),
    keras.layers.Dense(1)])
optimizer = keras.optimizers.RMSprop(0.001)

modelB.compile(loss='mean_squared_error',
    optimizer=optimizer,
    metrics=['mean_absolute_error', 'mean_squared_error'])


#train model
historyF = modelF.fit(trainData.index.values, trainData['f'], epochs=EPOCHS,
                    validation_split=0.2, verbose=0)
historyB = modelB.fit(trainData.index.values, trainData['b'], epochs=EPOCHS,
                    validation_split=0.2, verbose=0)

#test model
lossF, maeF, mseF = modelF.evaluate(testData.index.values, testData['f'], verbose=0)
print(maeF)
lossB, maeB, mseB = modelB.evaluate(testData.index.values, testData['b'], verbose=0)
print(maeB)

print('done')

predictionsF = modelF.predict(testData.index.values).flatten()
predictionsB = modelB.predict(testData.index.values).flatten()

print(predictionsF.min())
print(predictionsF.max())
print(np.histogram(predictionsF))

#avg = (predictionsF.min()+predictionsF.max())/2
for i in range(10):
    string = str(testData.index.values[i])
    if predictionsF[i] > np.median(predictionsF):
        string += ' f'
    if predictionsB[i] > np.median(predictionsB):
        string += ' b'
    print(string)
    print(str(predictionsF[i]) + ' ' + str(predictionsB[i]))
