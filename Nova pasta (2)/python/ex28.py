time1 = input('Digite o time 1: ')
time2 = input('Digite o time 2: ')
gols1 = int(input('Digite os gols do time 1: '))
gols2 = int(input('Digite os gols do time 2: '))

if (gols1 > gols2):
    print('{} venceu!!'. format(time1))
else:
    if (gols2 > gols1):
        print('{} venceu!!'. format(time2))
    else:
        print('Empate!!')        