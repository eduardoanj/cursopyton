horastrabalhadas = int(input('Digite as horas trabalhadas: '))
salporhora = int(input('Digite o salario por hora: '))
result = (horastrabalhadas * salporhora)
result2 = (result + (result /100 * 50))

if (horastrabalhadas > 40): 
    result2 = (result + (result /100 * 50))
    print('O salário do trabalhador é de: {}'. format(result2))
else:
    print('O salário do trabalhador é de: {}'. format(result))     