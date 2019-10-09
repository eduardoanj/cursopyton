#Ler um valor inteiro (aceitar somente valores entre 1 e 10) 
# e escrever a tabuada de 1 a 10 do valor lido.

valor = int(input('Digite um numero entre 0 e 10: '))
while (valor < 0) and (valor > 10):
    print('Valor invalido, digite um numero de 0 a 10')
    valor = int(input())

for i in range (0,11):
    i = i * valor
    print(i)
