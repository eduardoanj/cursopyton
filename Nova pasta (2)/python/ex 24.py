print('Digite o valor1, o valor2 e o valor3: ')
valor1 = int(input())
valor2 = int(input())
valor3 = int(input())

if (valor1 > valor2) and (valor1 > valor3):
    print('Omaior valor é: {}'. format(valor1))
else:
    if (valor2 > valor1) and (valor2 > valor3):
        print('O maior valor é: {}'. format(valor2))
    else:
        print('O maior valor é: {}'. format(valor3))        
