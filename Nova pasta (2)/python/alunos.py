

print('media geral dos alunos')
print('qual a quantidade de alunos')
qtd_alunos = int(input())
print('quantas notas por aluno')
qtd_notas = int(input())

soma_notas = 0

for aluno in range (0, qtd_alunos):
    #aluno = [0,1,2]
    for nota in range(0, qtd_notas):
        #nota= [0,1]
        print('aluno {} => nota {}'.format(aluno, nota))
        soma_notas = soma_notas + float(input())

media = soma_notas / (qtd_alunos * qtd_notas)
print ('media geral = {}'.format(media))        