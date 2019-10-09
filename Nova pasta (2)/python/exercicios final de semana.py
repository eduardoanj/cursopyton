'''
Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.
'''
'''
vetor = []
num = 0

for i in range (0, 5):
    print('Escreva o valor {}'.format(i + 1))
    num = int(input())
    vetor.append(num)

print('A sequencia de numeros é: {}'.format(vetor))
'''

'''
Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.
'''
'''
vetor = []
vet = 0

for i in range (0, 3):
    print('Digite o numero: ')
    vet = int(input())
    vetor.append(vet)

for i in range (len(vetor)-1, -1, -1):
    print(vetor[i])



'''
'''    
Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
'''
'''
notas = []
nota = 0
soma = 0
media = 0

for i in range (0, 4):
    print('Digite a {}ª nota'.format(i + 1))
    nota = float(input())
    notas.append(nota)

for i in range (0, 4):
    soma += notas[i]

media = soma / 4

print('as notas são: {}'.format(notas))
print('As médias são: {}'.format(media))    
'''
#Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.
'''
vetor =[]
consoantes = []
posição = 0

for i in range(0, 10, 1):
    letras = input('Digite as letras: ')
    vetor.append(letras)
    if vetor[i] != 'a' and vetor[i] != 'e' and vetor[i] != 'i' and vetor[i] != 'o' and vetor[i] != 'u':
        consoantes.append(vetor[i])
        posição += 1


print('Foram lidas {} consoantes, e elas são: {}'.format(posição, consoantes))
'''
'''
Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.
'''        
'''
vetor = []
vetor_par = []
vetor_impar = []

for i in range (0, 5):
    num = int(input('Digite um numero'))
    vetor.append(num)
    if (vetor[i] % 2) == 0:
        vetor_par.append(vetor[i])
    else:
        vetor_impar.append(vetor[i])           

print('Os numeros pares são {}, e os numeros ímpares são {}'.format(vetor_par, vetor_impar))             
'''       
#Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.

vetor = []
soma = []
media = []
notas = 0
alunos = []
media_aluno = []

for i in range (0, 10):
    alunos = []
    vetor.append(alunos)
    for j in range (0, 4):
        prec = float(input('Digite a {}ª nota do aluno '.format(i + 1)))
        alunos.append(prec)
        soma = soma + float(input())
    media = soma / 4    
    media_aluno.append(media)

for i in range(0, len(vetor)):
    for j in range(0, 4):
        print('aluno {}, nota {} = {}...média é de: {}'.format(i + 1, j + 1, vetor[i][j], media_aluno[i][j]))  


          