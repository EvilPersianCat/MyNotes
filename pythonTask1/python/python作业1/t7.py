x = int(input())
a = 0
count = 1
for i in range(1, x+1, 2):
    if count % 2 != 0:
        a += i
    else:
        a -= i
    count += 1
print(a)

