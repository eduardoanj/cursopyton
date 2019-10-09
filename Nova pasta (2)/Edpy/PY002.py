'''
Criar um programa que utilize o método 50-20-10-20: 
1. Leia o salário líquido informado pelo usuário.
2. Organize os valores de acordo com o método citado.
3. Informe ao usuário qual o valor que ele deve destinar para 
cada categoria
'''
# Método 50-20-10-20 (50% gastos, 20% investimentos a longo prazo,
#  10% investimentos a curto prazo, 20% livre)
'
salario = float(input('Digite o salário liquido '))

gastos = (salario / 100 * 50)
investimentos_lp = (salario / 100 * 20)
investimentos_cp = (salario / 100 * 10)
livre = (salario / 100 * 20)

print('O usuário deve usar R${} para gastos, R${} para investimentos a longo prazo, R${} para investimentos a curto prazo e sobram R${} livres. '.format(gastos, investimentos_lp, investimentos_cp, livre))
'