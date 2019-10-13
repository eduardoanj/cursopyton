distancia = int(input('Digite a distancia do destino: '))
preço_passagem= 0

if distancia < 200:
    preço_passagem = distancia * 0.5
else:
    preço_passagem = distancia * 0.45

print('O preço da passagem é de R${:.2f}'.format(preço_passagem))        

