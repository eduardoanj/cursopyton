#Escreva um algoritmo para ler 10 números e ao final da leitura 
#escrever a soma total dos 10 números lidos.

num = 0
valor10 = 0

for i in range(1, 11):
    print('Digite o numero {}:'.format(i))
    num = int(input())
    valor10 = num + valor10
print(valor10)