valor_casa = float(input('Escreva o valor da casa: '))
salario = float(input('Escreva o salario: '))
anos = int(input('Em quantos anos quer pagar? '))

prestação = (valor_casa / (anos*12))

if prestação <= (salario*0.3):
    print('A prestação é de R${:.2f}, então seu imprestimo foi APROVADO!'.format(prestação))
else:
    print('A prestação é de R${:.2f}, então seu emprestimo doi REPROVADO!'.format(prestação))    