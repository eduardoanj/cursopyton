#Uma loja está levantando o valor total de todas as mercadorias em estoque. Escreva um algoritmo que permita a entrada das seguintes informações: 
#a)	o número total de mercadorias no estoque; 
#b)	o valor de cada mercadoria.
#Ao final imprimir o valor total em estoque e a média de valor das mercadorias.
nummerc = int(input('Digite o numero de mercadorias: '))
valmerc = 0
somavalores = 0

for i in range (0, nummerc, 1):
    valmerc = int(input('Digite o valor da mercadoria {} '.format(i)))
    somavalores = somavalores + valmerc 

media = somavalores / nummerc
print('O valor total de estoque é: {}, e a média de valor é: {}'.format(somavalores, media))
