sexo = input('Digite o gênero (M ou F): ')
altura = float(input('Digite a altura: '))

if (sexo != 'm') and (sexo != 'M') and (sexo != 'f') and (sexo != 'F'):
    print('Sexo inválido ')

if (sexo == 'm') or (sexo == 'M'):
    result = (72.7 * altura) - 58
else:
    result = (62.1 * altura) - 44.7

print('O peso ideal é de: {:.2f}'. format(result)) 

     
