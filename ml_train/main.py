
from utils.util import getSequences
from keras.preprocessing import sequence
from keras.layers.embeddings import Embedding
from keras.layers.convolutional import MaxPooling1D
from keras.layers.convolutional import Conv1D
from keras.layers import LSTM
from keras.layers import Dense
from keras.models import Sequential
from keras.datasets import imdb
import numpy
import os
from sklearn.model_selection import train_test_split
# os.environ['CUDA_VISIBLE_DEVICES'] = '-1'
import tensorflow as tf

gpu = tf.config.experimental.list_physical_devices('GPU')
try:
    # Currently, memory growth needs to be the same across GPUs
    tf.config.experimental.set_memory_growth(gpu[0], True)
    logical_gpus = tf.config.experimental.list_logical_devices('GPU')
except RuntimeError as e:
    # Memory growth must be set before GPUs have been initialized
    print(e)

# LSTM and CNN for sequence classification in the IMDB dataset
# fix random seed for reproducibility
numpy.random.seed(7)
# load the dataset but only keep the top n words, zero the rest
top_words = 500

y = []
for i in range(200):
    y.append([1, 0, 0])

for i in range(200):
    y.append([0, 1, 0])

for i in range(200):
    y.append([0, 0, 1])

(X, y) = (numpy.array(getSequences()), numpy.array(y))
# print(X.shape)
# print(y.shape)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.33, random_state=42)
# truncate and pad input sequences
max_review_length = 500
# print(X_train, y_train)
X_train = sequence.pad_sequences(X_train, maxlen=max_review_length)
X_test = sequence.pad_sequences(X_test, maxlen=max_review_length)
print(X_train.shape)
# create the model
embedding_vecor_length = 32
model = Sequential()
model.add(Embedding(top_words, embedding_vecor_length,
                    input_length=max_review_length))
model.add(Conv1D(filters=32, kernel_size=3, padding='same', activation='relu'))
model.add(MaxPooling1D(pool_size=2))
model.add(LSTM(100))
model.add(Dense(3, activation='sigmoid'))
model.compile(loss='categorical_crossentropy',
              optimizer='adam', metrics=['accuracy'])
print(model.summary())
model.fit(X_train, y_train, epochs=30, batch_size=128,
          validation_data=(X_test, y_test))
# Final evaluation of the modelvvvvvvvvv
scores = model.evaluate(X_test, y_test, verbose=0)
print("Accuracy: %.2f%%" % (scores[1]*100))
model.save('./model.h5')
