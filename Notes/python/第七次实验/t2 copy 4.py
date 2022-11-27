table1=str.maketrans('1234567','一二三四五六日')
s1='1 3 4 9'
print(s1.translate(table1))
weeks={'1':'M一','2':'T二','3':'W三','4':'T四','5':'F五','6':'S六','7':'S日'}
table2=str.maketrans(weeks)
print(s1.translate(table2))