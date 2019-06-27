import tensorflow as tf
import pandas as pd
from tensorflow import keras
    
print("imported")

#read dataset
autoMpgNames = ['mpg', 'cylinders', 'displacement', 'horsepower',
                'weight', 'acceleration', 'model year', 'origin']  
data = pd.read_csv('auto-mpg.data', sep = ' ', skipinitialspace = True,
                   comment = '\t', names = autoMpgNames)
#remove '?' inputs

data = data[~data['horsepower'].isin(['?'])]
#remove NA inputs
data.dropna()
#split "Origin" into "USA", "Europe", "Japan" data
origin = data.pop('origin')
data['USA'] = (origin == 1)*1.0
data['Europe'] = (origin == 2)*1.0
data['Japan'] = (origin == 3)*1.0

#split into training/test sets
trainData = data.sample(frac=0.8)
testData = data.drop(trainData.index)

tStats = trainData.describe()
tStats.pop("mpg")
tStats = tStats.transpose()

#separate label from data
trainMpg = trainData.pop('mpg')
testMpg = testData.pop('mpg')

#norm the data (note: why?)
#this section isn't working; after 30 minutes, I've decided to use un-normed data
'''def norm(x):
  return (x - tStats['mean']) / tStats['std']
normedTrainData = norm(trainData)
normedTestData = norm(testData)
'''
normedTrainData=trainData
normedTestData=testData

print('building model')
#build model
model = keras.Sequential([
    keras.layers.Dense(64, activation=tf.nn.relu, input_shape=[len(normedTrainData.keys())]),
    keras.layers.Dense(64, activation=tf.nn.relu),
    keras.layers.Dense(1)
    ])
optimizer = tf.keras.optimizers.RMSprop(0.001)
model.compile(loss='mean_squared_error',
    optimizer=optimizer,
    metrics=['mean_absolute_error', 'mean_squared_error'])

#train model
early_stop = keras.callbacks.EarlyStopping(monitor='val_loss', patience=200)

EPOCHS = 10000
history = model.fit(normedTrainData, trainMpg, epochs=EPOCHS,
        validation_split = 0.2, verbose=0, callbacks=[early_stop])

#check against test set accuracy
loss, mae, mse = model.evaluate(normedTestData, testMpg, verbose=0)
print("Test set mean absolute error: {:5.2f} MPG".format(mae))

testPredictions = model.predict(normedTestData).flatten()
print('\nSample predictions:')
for i in range(5):
    print('Predicted MPG: %f. Actual MPG: %f' % (testPredictions[i], testMpg.tolist()[i]))
