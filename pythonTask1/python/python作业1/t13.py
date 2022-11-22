x = int(input())
mul = 1
for i in range(x, 0, -1):
    mul *= i
print(f'for循环结果{mul}')

mul = 1

while x != 0:
    mul *= x
    x -= 1
print(f'while循环结果{mul}')
