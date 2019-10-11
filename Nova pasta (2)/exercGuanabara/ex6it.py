salario = float(input('Digite o salario do funcionario: '))
aumento = 0
if salario > 1250:
    aumento = ((salario / 100) * 10) + salario
    print('O aumento do salario é de 10 porcento e foi para R${:.2f}'. format(aumento))
else:
    aumento = salario + ((salario / 100) * 15) 
    print('O aumento do salario é de 15 porcento e foi para R${:.2f}'.format(aumento))    
