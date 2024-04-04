import numpy as np
from sklearn import datasets
from sklearn import preprocessing
from keras.utils import np_utils


iris = datasets.load_iris()
scaler = preprocessing.StandardScaler()
scaler.fit(iris.data)
x = scaler.transform(iris.data)
print(x[:10])

# print(iris.data.shape)
# print(iris.target)