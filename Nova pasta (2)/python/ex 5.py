salario = int(input('Digite o salário: '))
reajuste = int(input('Digite o reajuste: '))

salliquido = (salario+(salario / 100 * reajuste))

print('O reajuste é de: {}%, o salário total é de: R${}'. format(reajuste, salliquido))