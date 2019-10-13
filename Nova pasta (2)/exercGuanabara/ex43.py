peso = float(input('Digite o peso'))
altura = float(input('Digite a altura'))

result = (peso / (altura**2))

if result < 18.5:
    print('Abaixo do peso: ')
elif result >= 18.5 and result < 25:
    print('Peso ideal')
elif result >= 25 and result < 30:
    print('sobrepeso')  
elif result >= 30 and result < 40:
    print('Obesidade')
elif result >= 40:
    print('Obesidade mórbida')             