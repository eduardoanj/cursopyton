salariofix = int(input('Digite o salário fixo: '))
numcarros = int(input('digite o número de carros vendidos: '))
comporcarro = int(input('Digite a comissão recebida por carro : '))
valorvendas = int(input('Digite o valor total de vendas: '))

valtotal = (valorvendas / numcarros )
porcentagem_por_carro = (valtotal / 100 * comporcarro)
salfinal = (salariofix + (valorvendas / 100 * 5))
result = (salfinal + porcentagem_por_carro)

print('O salario total é: R${} '. format(result))