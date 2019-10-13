lista = []
num = 0
for i in range(0, 3):
    num = int(input('Digite o numero {}: '.format(i+1)))
    lista.append(num)

print('O maior número é o {}, e o menor numero é o {}'.format(max(lista), min(lista)))

