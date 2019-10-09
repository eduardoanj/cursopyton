print('Digite valor1, valor2 e valor3: ')
valor1 = int(input())
valor2 = int(input())
valor3 = int(input())
soma = 0

if (valor1 > valor2) and (valor2 > valor3): 
    soma = valor1 + valor2

if (valor1 > valor3) and (valor3 > valor2):
    soma = valor1 + valor3

if (valor2 > valor1) and (valor1 > valor3):
    soma = valor2 + valor1

if (valor2 > valor3) and (valor3 > valor1):
    soma = valor2 + valor3

if (valor3 > valor1) and (valor1 > valor2):
    soma = valor3 + valor1

if (valor3 > valor2) and (valor2 > valor1):
    soma = valor3 + valor2            


print('A soma dos dois maiores é de: {}'. format(soma))
