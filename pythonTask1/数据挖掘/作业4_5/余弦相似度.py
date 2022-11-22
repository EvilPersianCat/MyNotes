import numpy as np
import scipy.spatial.distance as dist  # 导入scipy距离公式

t1  = np.array([0, 1, 0, 1])
t2  = np.array([1, 0, 1, 0])

def cos_sim(a, b):
    a_norm = np.linalg.norm(a)
    b_norm = np.linalg.norm(b)
    cos = np.dot(a,b)/(a_norm * b_norm)
    return cos

def eucliDist(a,b):
    return np.sqrt(sum(np.power((a - b), 2)))

def jaccard(a,b):    
    matV = np.mat([a,b])
    return dist.pdist(matV,'jaccard')

def SimpleMatching(a,b):
     matV = np.mat([a,b])
     return dist.pdist(matV,'matching')

print('余弦相似度:',end=" ")
print(cos_sim(t1,t2))

print('欧氏距离:',end=" ")
print(eucliDist(t1,t2))

print('jaccard:',end=" ")
print(jaccard(t1,t2))

print('简单匹配距离:',end=" ")
print(SimpleMatching(t1,t2))




