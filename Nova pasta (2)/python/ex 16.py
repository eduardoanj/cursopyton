print('Digite o valor 1 e o valor 2 ')
valor1 = int(input())
valor2 = int(input())

if (valor1 == valor2):
    print('Osvalores são iguais ')
else:
    if (valor1 > valor2):
        print ('{}, {}'. format(valor2, valor1))
    else:
        print ('{}, {}'. format(valor1, valor2))        