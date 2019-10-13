num1 = 1
num2 = 2
num3 = 3
print(num1)
print(num2)
print(num3)
cont = 3

def cal_fibo():
    global num1
    global num2
    global num3
    num1 = num3 + num2
    print(num1)
    num2 = num1 + num3
    print(num2)
    num3 = num1 + num2
    print(num3)

for i in range(0, 10):
    cal_fibo()
