from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

iris = load_iris()
# 从sklearn数据集中获取鸢尾花数据
iris_feature = iris.data
iris_label = iris.target
# 将数据划分为训练集和测试集
# test_size=0.3表示测试集占0.3，训练集占0.7
# random_state相当于随机数种子random.seed()
x_train, x_test, y_train, y_test = train_test_split(iris_feature, iris_label, test_size=0.3, random_state=30)
knn = KNeighborsClassifier(n_neighbors=5, algorithm='auto', weights='distance', n_jobs=1)
knn.fit(x_train, y_train)
predict = knn.predict(x_test)
# 预测结果
print(predict)
# 原本测试数据
print(y_test)
# 准确性
print(accuracy_score(predict, y_test))
