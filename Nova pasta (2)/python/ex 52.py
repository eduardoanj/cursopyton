#Ler 2 valores, calcular e escrever a soma dos inteiros existentes 
#entre os 2 valores lidos (incluindo os valores lidos na soma). 
#Considere que o segundo valor lido será sempre maior que o 
#primeiro valor lido.

num = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))
num3 = 0

for i in range (num, num2 +1):
    num3 += i 
    
print(num3)

