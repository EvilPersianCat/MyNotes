import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import preprocessing

data = pd.read_excel("cckstrain.xls")

x = data.iloc[:, 1:7]
y = data.iloc[:, 7:]

x = x.drop(columns=["Quality"])

x[["Enterprise", "Destination", "Origin", "Custom"]] = np.array(
    x[["Enterprise", "Destination", "Origin", "Custom"]], dtype=np.string_
)

le = preprocessing.LabelEncoder()

for col in x.columns.values:
    if x[col].dtypes == "|S10":
        le.fit(x[col])
        x[col] = le.transform(x[col])


X_train, X_test, Y_train, Y_test = train_test_split(
    x, y, test_size=1 / 3, random_state=10
)


KNN = KNeighborsClassifier(
    n_neighbors=5, algorithm="auto", weights="distance", n_jobs=1
)

KNN.fit(X_train, Y_train)

score_train = KNN.score(X_train, Y_train)
score_test = KNN.score(X_test, Y_test)

print("训练集分数: " + str(score_train))
print("测试集分数: " + str(score_test))


data_pre = pd.read_excel("CCKStest3 .xlsx")
X_pre = data_pre.iloc[:, :5]


X_pre[["Enterprise", "Destination", "Origin", "Custom"]] = np.array(
    X_pre[["Enterprise", "Destination", "Origin", "Custom"]], dtype=np.string_
)

for col in X_pre.columns.values:
    if X_pre[col].dtypes == "|S10":
        le.fit(X_pre[col])
        X_pre[col] = le.transform(X_pre[col])

Y_pre = KNN.predict(X_pre)
print(Y_pre)

resp = pd.DataFrame(Y_pre)
resp.to_excel("Product1.xlsx")
