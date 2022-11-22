from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import graphviz
import os
os.environ["PATH"] += os.pathsep + 'C:/Program Files/Graphviz/bin/'

iris = load_iris()  # 从sklearn 数据集中获取鸢尾花数据。

iris = load_iris()   	# 准备数据集
features = iris.data	# 获取特征集
labels = iris.target    # 获取目标集

train_features, test_features, train_labels, test_labels = train_test_split(features, labels, test_size=0.33, random_state=0)

# 用CART 算法构建分类树（你也可以使用ID3 算法构建）
clf = DecisionTreeClassifier()

# 用训练集拟合构造CART分类树
clf = clf.fit(train_features, train_labels)

test_predict = clf.predict(test_features)

score = accuracy_score(test_labels, test_predict)
score2 = clf.score(test_features, test_labels)
print(score, score2)

# clf 为决策树对象
dot_data = tree.export_graphviz(clf)
graph = graphviz.Source(dot_data)

# 生成 Source.gv.pdf 文件，并打开
graph.view()

