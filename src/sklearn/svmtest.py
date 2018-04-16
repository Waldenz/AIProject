from sklearn import  datasets

#向python对象载入数据：
iris = datasets.load_iris()
#digits = datasets.load_digits()
#数据存储在.data项中，是一个(n_samples, n_features)数组。
iris.data.shape

from sklearn import svm

clf = svm.LinearSVC()
clf.fit(iris.data, iris.target) # learn from the data
# LinearSVC(C=1.0, class_weight=None, dual=True, fit_intercept=True,
#      intercept_scaling=1, loss='l2', multi_class='ovr', penalty='l2',
#      tol=0.0001, verbose=0)
#一旦我们已经从数据学习，我们可以使用我们的模型来预测未观测数据最可能的结果。
print(clf.predict([[ 5.0,  3.6,  1.3,  0.25]]))
