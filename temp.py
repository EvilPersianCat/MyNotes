import re
phone_number = input("输入手机号\n")
zip_code = input("输入邮编\n")
url = input("输入网址\n")
if re.match(r'1[3|4|5|7|8]\d{9}',phone_number):
    print("输入的手机号格式正确")
else:
    print("输入的手机号格式错误\n")
if re.match(r'^[1-9]\d{5}$',zip_code):
    print("输入的邮编格式正确\n")
else:
    print("输入的邮编格式错误\n")
if re.match(r'(http|ftp|https)://[\w\-_]+(\.[\w\-_]+)+([\w\-\.,@?^=%&:/~\+#]*[\w\-\@?^=%&/~\+#])?',url):
    print("输入的网址格式正确\n")
else:
    print("输入的网址格式错误\n")
