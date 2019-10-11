ver = 1
num0 = 0
print(num0)
num1 = 1
print(num1)
num2 = 2
print(num2)
fibo = []
reverse = []
num0 = num1 + num2
fibo.append(num0)
print(num0)

while num2 > 0:
    last = fibo[-1] + fibo[-2]
    fibo.append(last)
    print(fibo[-1])
