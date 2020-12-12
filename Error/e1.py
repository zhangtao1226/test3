# 1、除法或求模时第二个参数为零时的错误
try:
    x = int(input('Enter this first number: '))
    y = int(input("Enter this second number: "))
    print(x / y)
except Exception as e:
    print(e)



