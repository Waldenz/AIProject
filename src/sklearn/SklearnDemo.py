

from sklearn import svm
X = [[0, 0], [1, 1]]
y = [0, 1]
clf = svm.SVC()
clf.fit(X, y)
print(clf)
''' clf详情
SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0,
    decision_function_shape='ovr', degree=3, gamma='auto', kernel='rbf',
    max_iter=-1, probability=False, random_state=None, shrinking=True,
    tol=0.001, verbose=False)

经常用到sklearn中的 svm.SVC 函数，这个函数也是基于libsvm实现的，所以在参数设置上有很多相似的地方。（libsvm中的二次规划问题的解决算法是SMO） 
 
参数： 
    C：C-SVC的惩罚参数C  默认值是1.0  
        C越大，越惩罚 松弛变量（误分类），希望 松弛变量（误分类） 接近0，趋向于对训练集全分对的情况，对训练集测试时准确率很高，但泛化能力弱。 
            【泛化能力(generalization ability)是指机器学习算法对新鲜样本的适应能力。学习的目的是学到隐含在数据对背后的规律， 
            对具有同一规律的学习集以外的数据，经过训练的网络也能给出合适的输出，该能力称为泛化能力。】 
        C值小，对误分类的惩罚减小，允许容错，将他们当成噪声点，泛化能力较强。 
         
    kernel ：核函数，默认是rbf，可以是‘linear’, ‘poly’, ‘rbf’, ‘sigmoid’, ‘precomputed’  
      　　0 – 线性：u'v 
     　　 1 – 多项式：(gamma*u'*v + coef0)^degree 
      　　2 – RBF函数：exp(-gamma|u-v|^2) 
      　　3 –sigmoid：tanh(gamma*u'*v + coef0) 
   degree ：多项式poly函数的维度，默认是3，选择其他核函数时会被忽略。 
   gamma ： ‘rbf’,‘poly’ 和‘sigmoid’的核函数参数。默认是’auto’，则会选择1/n_features 
   coef0 ：核函数的常数项。对于‘poly’和 ‘sigmoid’有用。 
   probability ：是否采用概率估计？.默认为False 
   shrinking ：是否采用shrinking heuristic方法，默认为true 
   tol ：停止训练的误差值大小，默认为1e-3 
   cache_size ：核函数cache缓存大小，默认为200 
   class_weight ：类别的权重，字典形式传递。设置第几类的参数C为weight*C(C-SVC中的C) 
   verbose ：允许冗余输出？ 
   max_iter ：最大迭代次数。-1为无限制。 
   decision_function_shape ：‘ovo’, ‘ovr’ or None, default=None3 
   random_state ：数据洗牌时的种子值，int值 
主要调节的参数有：C、kernel、degree、gamma、coef0。 
'''
print(clf.predict([[1,2]]))
# get support vectors
print(clf.support_vectors_)
# get indices of support vectors 得到支持向量指数
print(clf.support_)
# get number of support vectors for each class  获取每个类的支持向量数
print(clf.n_support_)