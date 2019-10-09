#Ler o número de alunos existentes em uma turma e, 
# após isto, ler as notas destes alunos, 
# calcular e escrever a média aritmética dessas notas lidas.

numalunos = int(input('Digite o numero de alunos: '))

valor10 = 0

for i in range (0, numalunos):
    print('digite o valor: {}'.format(i))
    valor = int(input())
    valor10 = valor10 + valor

media = valor10 / numalunos
print('a media é {}'.format(media))         
