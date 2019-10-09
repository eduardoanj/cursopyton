#Escreva um algoritmo para ler 10 números. 
# Todos os números lidos com valor inferior a 40 
# devem ser somados. 
# Escreva o valor final da soma efetuada.

valorinf = 0
valor = 0

for i in range(1, 11):
    print('Escreva o valor {}'.format(i))
    valor = int(input())
    if (valor < 40):
        valorinf += valor

print('A soma dos valores é de {}'.format(valorinf))         