#Ler 10 valores, calcular e escrever a média aritmética desses valores lidos.

valor10 = 0

for i in range (1, 11):
    print('digite o valor: {}'.format(i))
    valor = int(input())
    valor10 = valor10 + valor

media = valor10 / 10
print('a media é {}'.format(media))