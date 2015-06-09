#!/usr/bin/python
#coding=utf-8
"""
PCA分析
寻找合适的特征数
The sklearn provides an object that, 
given data, computes the score during the fit of an estimator on a parameter grid 
and chooses the parameters to maximize the cross-validation score. 

>>> from sklearn.grid_search import GridSearchCV
>>> Cs = np.logspace(-6, -1, 10)
>>> clf = GridSearchCV(estimator=svc, param_grid=dict(C=Cs),
...                    n_jobs=-1)
>>> clf.fit(X_digits[:1000], y_digits[:1000])        
GridSearchCV(cv=None,...
>>> clf.best_score_                                  
0.925...
>>> clf.best_estimator_.C                            
0.0077...
"""
print(__doc__)

from sklearn import linear_model, decomposition, datasets
from sklearn.pipeline import Pipeline
from sklearn.grid_search import GridSearchCV
import matplotlib.pyplot as plt
import numpy as np

logistic = linear_model.LogisticRegression()

pca = decomposition.PCA()
pipe = Pipeline(steps=[('pca', pca), ('logistic', logistic)])

digits = datasets.load_digits()
X_digits = digits.data
y_digits = digits.target
print len(X_digits),X_digits.shape,len(y_digits),y_digits.shape

###############################################################################
# Plot the PCA spectrum
pca.fit(X_digits)
print '64:\n',pca.explained_variance_.shape

# pca.explained_variance_.sort()
# print pca.explained_variance_

plt.figure(1, figsize=(4, 3))
plt.clf()
plt.axes([.2, .2, .7, .7])
plt.plot(pca.explained_variance_, linewidth=2)
plt.axis('tight')
plt.xlabel('n_components')
plt.ylabel('explained_variance_')

###############################################################################
# Prediction

n_components = [20,40,60]
Cs = np.logspace(-4, 4, 3)#对数（若没说明，一般是底为10）坐标下的均匀取点
print Cs

#Parameters of pipelines can be set using ‘__’ separated parameter names:

estimator = GridSearchCV(pipe,
                         dict(pca__n_components=n_components,
                              logistic__C=Cs))
estimator.fit(X_digits, y_digits)
print estimator
print estimator.best_score_
print estimator.best_params_
print estimator.best_estimator_



plt.axvline(estimator.best_estimator_.named_steps['pca'].n_components,
            linestyle=':', label='n_components chosen')
plt.legend(prop=dict(size=12))
print estimator.best_estimator_.named_steps['pca'].n_components
# plt.show()