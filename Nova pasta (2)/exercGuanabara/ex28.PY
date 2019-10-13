from random import randint

rand = randint(0, 5)

num = int(input('Digite um numero'))

if num == rand:
    print('Parabens, voce acertou')
else:
    print('voce errou')    

