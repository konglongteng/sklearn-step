#!/usr/bin/python
#coding=utf-8

# from sklearn import datasets
# iris = datasets.load_iris()
# # print iris
# # Matrix sampleNum * Features
# print iris.data.shape

# digits = datasets.load_digits()
# print digits.images.shape

# import pylab as pl
# pl.imshow(digits.images[-1], cmap=pl.cm.gray_r) 
# # pl.show()


import numpy as np
from sklearn import datasets
iris = datasets.load_iris()
iris_X = iris.data
iris_y = iris.target
print np.unique(iris_y)

