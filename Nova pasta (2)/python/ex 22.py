quantidadeatual = int(input('Digite a quantidade atual em estoque: '))
quantidademaxima = int(input('Digite a quantidade maxima: '))
quantmini = int(input('Digite a quantidade minima: '))

quantmedia = ((quantidademaxima + quantmini) / 2)

if (quantidadeatual >= quantmedia):
    print('Não efetuar compra')
else:
    print('Efetuar compra')
        