valor1 = int(input('Escreva o valor 1: '))
valor2 = int(input('Escreva o valor 2: '))

while (valor2 == 0):
    print('valor 2 não pode ser zero, digite um novo valor: ')
    valor2 = int(input())

resultado = (valor1 / valor2)
print('valor1 / valor2 = {}'. format(resultado))
