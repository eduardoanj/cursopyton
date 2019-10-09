#Modifique o exercício anterior para aceitar somente valores maiores que 0 
# para N. Caso o valor informado (para N) não seja maior que 0,
#  deverá ser lido um novo valor para N.

n = int(input('Digite um valor: '))
while (n <= 0):
    print('Digite um numero maior que zero')
    n = int(input())

for i in range(0, n):
    i = i + 1
    print(i)