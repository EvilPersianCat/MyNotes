from sklearn import tree
import random

X = [[42, 10], [25, 18], [33, 11], [55, 10], [16, 33], [10, 20], [15, 17], [23, 21], [50, 20], [20, 34]]
Y = [0, 1, 0, 1, 1, 0, 1, 0, 0, 1]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, Y)

demo1 = [[random.random() * 100, random.random() * 100],
         [random.random() * 100, random.random() * 100],
         [random.random() * 100, random.random() * 100]]

print(demo1)

print(clf.predict(demo1))
print(clf.predict_proba(demo1))  # 计算属于每个类的概率
