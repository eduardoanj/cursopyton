#Faça um algoritmo para ler o código e o preço de 15 produtos, calcular e escrever: 
#•	o maior preço lido.
#•	a média aritmética dos preços dos produtos.

codigo = 0
preço = 0
maior = 0
somapreço = 0
media = 0
numeros =[]

for i in range (0, 15, 1):
    print('Escreva o codigo: ')
    codigo = int(input())
    print('Escreva o valor do produto: ')
    preço = int(input())  
    numeros.append(preço)
    somapreço = somapreço + preço

media = somapreço / 15
print ('Maior número da lista: ', max(numeros))
print ('A média aritmética é {}'.format(media)) 
