#Escreva um algoritmo para ler as notas da 1a. e 2a. avaliações de um aluno, 
# calcule e imprima a média (simples) desse aluno. 
# Só devem ser aceitos valores válidos durante a 
# leitura (0 a 10) para cada 

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

while (nota1 < 0) or (nota1 > 10):
    print('Nota inválida, digite um valor entre 0 e 10: ')
    nota1 = float(input())

while (nota2 < 0) or (nota2 > 10):
    print('Nota inválida, digite um valor entre 0 e 10: ')
    nota2 = float(input())

media = ((nota1 + nota2) / 2)

print('A média do aluno é de {}.'.format(media))
