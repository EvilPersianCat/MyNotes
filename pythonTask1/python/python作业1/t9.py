for i in range(1, 10):
    for j in range(1, i+1):
        print(f"{j} * {i} = {i * j}", end="\t")
    print()

print()

for i in range(9, 0, -1):
    for j in range(1, i+1):
        print(f"{j} * {i} = {i * j}", end="\t")
    print()

print()

for i in range(1, 10):
    for j in range(1, 10):
        print(f"{j} * {i} = {i * j}", end="\t")