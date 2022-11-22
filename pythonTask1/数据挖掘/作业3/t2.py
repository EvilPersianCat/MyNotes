from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import graphviz
import os

os.environ["PATH"] += os.pathsep + 'C:/Program Files/Graphviz/bin/'

iris = load_iris()

iris = load_iris()
features = iris.data
labels = iris.target

train_features, test_features, train_labels, test_labels = train_test_split(features, labels, test_size=0.33, random_state=0)

clf = DecisionTreeClassifier()

clf = clf.fit(train_features, train_labels)

test_predict = clf.predict(test_features)

score = accuracy_score(test_labels, test_predict)
score2 = clf.score(test_features, test_labels)
print(score, score2)

dot_data = tree.export_graphviz(clf)
graph = graphviz.Source(dot_data)

graph.view()

