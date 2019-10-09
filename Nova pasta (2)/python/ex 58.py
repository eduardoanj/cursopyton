'''
 A prefeitura de uma cidade deseja fazer uma pesquisa entre seus habitantes. Faça um algoritmo para coletar dados sobre o salário e número de filhos de cada habitante e após as leituras, escrever: 
a)	Média de salário da população 
b)	Média do número de filhos 
c)	Maior salário dos habitantes 
d)	Percentual de pessoas com salário menor que R$ 150,00 
Obs.: O final da leitura dos dados se dará com a entrada de um “salário negativo”.
'''
salario = 0
numfilhos = 0
maiorsal = 0
salabaixo = 0
repetições = 0
medsal = 0
medfil = 0
numeros = []
salmin = 0

while (salario >= 0):
    print('Digite o salario: ')
    salario = float(input())
    medsal = medsal + salario
    print('Media de filhos: ')
    numfilhos = float(input())
    medfil = medfil + numfilhos
    repetições = repetições + 1
    numeros.append(salario)
    if (salario < 150):
        salmin = salmin + 1
if (salario < 0):
    print('salario negativo')  
    
percentsalmin = salmin * 100 / repetições
mediasalario = medsal / repetições
mediafilhos = medfil / repetições

print('A media de salario da população é {:.2f},\n A media de filhos é de {:.2f}, \n O maior salario é {:.2f}, e o percentual de pessoas com o salario menor que R$150,00 é de {:.2f}'.format(mediasalario, mediafilhos, max(numeros), percentsalmin ))