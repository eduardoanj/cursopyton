num = []

repeticao = 3
contador = 0

while repeticao != 0:
    repeticao = int(input('Digite um número: (0 para sair)'))
    num.append(repeticao)
    contador += 1

contador = contador - 1
media = sum(num)/contador

print('A média dos números digitados é de: {:.2f}'.format(media))
