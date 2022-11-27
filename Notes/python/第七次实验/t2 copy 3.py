s1='one,two,three'
print(s1.split(','))
print(s1.rsplit(',', 1))
print(s1.partition(','))
print(s1.rpartition(','))
s2='abc\n123\nxyz'
print(s2.splitlines())
print(s2.splitlines(True))
s3= ('a','b','c')
s4=':'
print(s4.join(s3))
print(s4.join('123'))
