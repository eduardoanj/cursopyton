ano_nascimento = int(input('Digite o ano de nascimento: '))

praso = 0

if ano_nascimento < 2001:
    praso = 2019 -((18 - (2001 - ano_nascimento))+2001)
    print('Voce já se alistou ao serviço militar, voce se alistou a {} anos atras'.format(praso))
elif ano_nascimento > 2001:
    praso = (18 - (2019 - ano_nascimento)) + 2019
    print('Voce ainda não se alistou ao serviço militar, poderá se alistar até {}'.format(praso))  
elif ano_nascimento == 2001:
    print('é hora para se alistar ao serviço militar')      