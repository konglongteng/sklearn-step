#!/usr/bin/python
#coding=utf-8
"""
================================
SVM Exercise
================================

A tutorial exercise for using different SVM kernels.

1,导入dataset,找到X（samples）和y（Lables）
2,设定X_train X_test  y_train y_test
3,fit
4,predict

"""
print(__doc__)

import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets, svm

# 载入数据，打乱顺序，分配train和test
iris = datasets.load_iris()
X = iris.data
y = iris.target
n_sample = len(X)
np.random.seed(0)
order = np.random.permutation(n_sample)
# print order
X = X[order]
y = y[order].astype(np.float)
# print y

X_train = X[:.9 * n_sample]
y_train = y[:.9 * n_sample]
X_test = X[.9 * n_sample:]
y_test = y[.9 * n_sample:]

# fit model
clf = svm.SVC(kernel='linear', gamma=10)
clf.fit(X_train, y_train)
Z = clf.predict(X_test)
print Z
print y_test


# print clf.fit(X_train, y_train).score(X_test, y_test)



