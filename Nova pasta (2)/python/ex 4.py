numbrancos = int(input('Digite o numero de votos brancos: '))
numnulos = int(input('Digite o numero de votos nulos: '))
numvalidos = int(input('Digite o numero de votos válidos: '))

numtotal = (numbrancos + numnulos + numvalidos)

brapercent = ((numbrancos * 100) / numtotal)
nulpercent = ((numnulos * 100) / numtotal)
valpercent = ((numvalidos * 100) / numtotal)

print('Total de votos: {}, brancos: {}%, nulos: {}%. válidos: {}%'. format(numtotal, brapercent, nulpercent, valpercent))