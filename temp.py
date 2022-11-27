s = 'babad'
n = len(s)
for L in range(n, 0, -1):
    for i in range(n):
        j = i + L - 1
        if j >= n:
            break
        temp = s[i:j+1]
        if temp == temp[::-1]:
            print(L)        
        
print(1)