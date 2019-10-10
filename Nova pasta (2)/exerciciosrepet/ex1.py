jogadores = []

jogador = int(input('Digite o numero de jogadores'))


for i in range(1, jogador+1):
    altura = float(input(f'Digite a altura do jogador {i} '))
    jogadores.append(altura)

media = (sum(jogadores) )/ jogador
print('A media de altura dos jogadores é de {:.2f}m'.format(media))