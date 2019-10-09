salfixo = float(input('Digite o salário fixo: '))
vendas = float(input('Digite o valor total de vendas: '))

if (vendas > 1500):
    result = (salfixo + (vendas / 100 * 8))
else:
    result = (salfixo + (vendas / 100 * 3))

print('O salário total é de: R${}'. format(result) )        