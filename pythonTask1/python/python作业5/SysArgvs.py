import sys
print("参数个数：", len(sys.argv))
for i,x in enumerate(sys.argv):
    print("argv[{0}] = {1}".format(i, x))