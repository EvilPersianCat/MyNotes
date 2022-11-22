from calendar import *
def ndays(y, m):
    monthDay = [31,28,31,30,31,30,31,31,30,31,30,31]
    days = monthDay[ m-1 ]
    if m == 2 and isleap(y):
        days += 1
    return days

y = int( input('请输入（>=1）,否则1：') )
m = int( input('请输入（1~12）,否则<1为1、>12为12：') )
if y < 1: y = 1
if m < 1: m = 1
if m > 12: m = 12
print( ndays(y,m) )
