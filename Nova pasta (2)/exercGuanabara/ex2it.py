velocidade = int(input('Digite a velocidade do carro: '))
multa = 0

if velocidade < 80:
    print('Velocidade ok')
else:
    multa = (velocidade * 7)
    print('Voce foi multado, o valor da multa é de R${}'.format(multa))

    