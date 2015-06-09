#!/usr/bin/python
#coding=utf-8

"""
Vector Quantization Example
Lena 512*512
Here to illustrate hwo K-means is used for vector quantization
K-Means算法可以压缩信息，将512*512的图像量化为5个等级

"""

print (__doc__)


import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

from sklearn import cluster

n_clusters = 5
np.random.seed(0)

try:
    lena = sp.lena()
except AttributeError:
    # Newer versions of scipy have lena in misc
    from scipy import misc
    lena = misc.lena()
X = lena.reshape((-1, 1))  # We need an (n_sample, n_feature) array
print X
k_means = cluster.KMeans(n_clusters=n_clusters, n_init=4)
k_means.fit(X)
values = k_means.cluster_centers_.squeeze()
labels = k_means.labels_
print values #聚类中心
print labels #这里将图像已经分类
print len(X),len(labels)





# create an array from labels and values
lena_compressed = np.choose(labels, values)
lena_compressed.shape = lena.shape

vmin = lena.min()
vmax = lena.max()

# original lena
plt.figure(1, figsize=(3, 2.2))
plt.imshow(lena, cmap=plt.cm.gray, vmin=vmin, vmax=256)

# compressed lena
plt.figure(2, figsize=(3, 2.2))
plt.imshow(lena_compressed, cmap=plt.cm.gray, vmin=vmin, vmax=vmax)

# # equal bins lena
# regular_values = np.linspace(0, 256, n_clusters + 1)
# regular_labels = np.searchsorted(regular_values, lena) - 1
# regular_values = .5 * (regular_values[1:] + regular_values[:-1])  # mean
# regular_lena = np.choose(regular_labels.ravel(), regular_values)
# regular_lena.shape = lena.shape
# plt.figure(3, figsize=(3, 2.2))
# plt.imshow(regular_lena, cmap=plt.cm.gray, vmin=vmin, vmax=vmax)

# # histogram
# plt.figure(4, figsize=(3, 2.2))
# plt.clf()
# plt.axes([.01, .01, .98, .98])
# plt.hist(X, bins=256, color='.5', edgecolor='.5')
# plt.yticks(())
# plt.xticks(regular_values)
# values = np.sort(values)
# for center_1, center_2 in zip(values[:-1], values[1:]):
#     plt.axvline(.5 * (center_1 + center_2), color='b')

# for center_1, center_2 in zip(regular_values[:-1], regular_values[1:]):
#     plt.axvline(.5 * (center_1 + center_2), color='b', linestyle='--')

plt.show()