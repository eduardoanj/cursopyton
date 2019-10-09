print('Digite valor 1 e valor 2: ')
valor1 = int(input())
valor2 = int(input())
#para comparar valores se digita2 iguais "=="
if (valor1 == valor2):
    print('os valores são iguais ')
else:
    if (valor1 > valor2):
        print('O valor {} é maior'. format(valor1)) 
    else:
        print('O valor {} é maior'. format(valor2))       
