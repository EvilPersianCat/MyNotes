from sklearn.datasets import load_iris
import pydotplus #引入pydotplus
from sklearn import tree

X = [
    [1, 0, 1],
    [0, 1, 1],
    [0, 0, 0],
    [1, 1, 1],
    [0, 2, 1],
    [0, 1, 0],
    [1, 2, 1],
    [0, 0, 1],
    [0, 1, 0],
    [0, 0, 1]
]

Y = [0, 0, 0, 0, 1, 0, 0, 1, 0, 1]

mode = tree.DecisionTreeClassifier()

clf = mode.fit(X, Y)

dot_data = tree.export_graphviz(clf, out_file=None)
graph = pydotplus.graph_from_dot_data(dot_data)
graph.write_pdf("fyy.pdf")#将图写成pdf文件


