#O mesmo exercício anterior, mas agora, considere que o segundo valor lido poderá ser maior ou menor que o primeiro valor lido, ou seja, deve-se testá-los.


num = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))
num3 = 0

if (num < num2):
    for i in range (num, num2 +1):
        num3 += i 
    
if (num > num2):
    for i in range (num2, num +1):
        num3 += i    

print(num3)
