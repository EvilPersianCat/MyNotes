# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 09:31:10 2022

@author: zhenkai
"""

from sklearn import datasets
from sklearn.model_selection import GridSearchCV, train_test_split, cross_val_score

iris = datasets.load_iris()  # 下载鸢尾花数据集
data_x = iris["data"]  # 特征x
# print(data_x)
data_y = iris["target"]  # 类别y
# 将每一列特征划分成几份区间，标准化
num_1 = 5  # 每个特征分成五份，我这里是每个特征都分成5个区间，也可以分开。不过代码自己改


def standard_feature(feature_col, num):
    max_0 = max(data_x[:, feature_col])
    min_0 = min(data_x[:, feature_col])
    width_0 = (max_0 - min_0) / num
    for j in range(len(data_x[:, feature_col])):
        for i in range(1, num + 1):
            if min_0 + (i - 1) * width_0 <= data_x[j, feature_col] <= min_0 + i * width_0:
                data_x[j, feature_col] = i
                # print(data_x[j,feature])
                break


x_col_num = len(data_x[0])  # 获取列数及特征数目


def get_pb(one_feature, col, x_train):
    '''
    one_feature在该x_train数据集的col列的概率
    :param one_feature:查找的特征是啥
    :param col: 列
    :param x_train:
    :return: 返回该特征的概率
    '''
    fea_sum = 0
    for i in x_train[:, col]:
        if i == one_feature:
            fea_sum += 1
    col_all = len(x_train)
    p_b1 = fea_sum / col_all
    # if p_b1 == 0:
    #     print("第几列第几个特征个数为0",col,one_feature,len(x_train))#如果当你把x特征分的太细会出现有些特征测试集有但训练集没有。看len(x_train）当这个等于训练集总数第78行会除数为0
    return p_b1


for i in range(x_col_num):  # data_x将所有特征标准化
    standard_feature(i, num_1)
x_train, x_test, y_train, y_test = train_test_split(data_x, data_y, test_size=0.3)  # 拆分成测试集，训练集
print("训练集样本数量", len(x_train))
print("测试集样本数量", len(x_test))

test_PB_list = []  #
for row_i in range(len(x_test)):
    P_B = 1
    for col_i in range(x_col_num):
        one_pb = get_pb(x_test[row_i, col_i], col_i, x_train)
        P_B *= one_pb
    # 经过for循环得到每个测试集样本的P（B）
    test_PB_list.append(P_B)
print("test_PB_list元素个数", len(test_PB_list))
y = 3
y_index_list = []  # 分别存放对应y的全部训练集的全部列索引，该列表元素的列表索引对应y
for y_num in range(y):
    one_y_index_list = []
    for y_index in range(len(y_train)):
        if y_train[y_index] == y_num:
            one_y_index_list.append(y_index)
    y_index_list.append(one_y_index_list)
print("训练集中每类拥有索引个数", *[len(a) for a in y_index_list])
y_num_list = []
for y_num in range(y):
    one_y_num = 0
    for y_index in range(len(y_train)):
        if y_train[y_index] == y_num:
            one_y_num += 1
    y_num_list.append(one_y_num)
print("训练集每类拥有个数", y_num_list)
test_y_predict = []  # 测试集预测Y
for test_row in range(len(x_test)):  # test_row为测试集每行样本，每行样本都需要计算分类为各个y的概率，哪个概率最大，说明就是哪一类
    final_y_P = []
    for y_index in range(y):
        x_train_yindex = x_train[y_index_list[y_index], :]
        P_BinA = 1
        for col_i in range(x_col_num):
            one_pb = get_pb(x_test[test_row, col_i], col_i, x_train_yindex)
            P_BinA *= one_pb
        PAinB = (y_num_list[y_index] / len(y_train)) * P_BinA / test_PB_list[test_row]
        final_y_P.append(PAinB)
    belong_class = final_y_P.index(max(final_y_P))
    test_y_predict.append(belong_class)
print(test_y_predict)
print(list(y_test))
predict_right_num = 0
for i in range(len(test_y_predict)):
    if test_y_predict[i] == y_test[i]:
        predict_right_num += 1
probability = predict_right_num / len(test_y_predict)
print("预测正确概率", probability)
