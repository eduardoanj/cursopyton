'''
1) Escreva um algoritmo que permita a leitura dos nomes de 10 pessoas e armazene os nomes lidos em um vetor. Após isto, o algoritmo deve permitir a leitura de mais 1 nome qualquer de pessoa e depois escrever a mensagem ACHEI, se o nome estiver entre os 10 nomes lidos anteriormente (guardados no vetor), ou NÃO ACHEI caso contrário.
'''
'''
nomes = []

for i in range (0, 3, 1):
    print('Digite um nome: ')
    nomes.append(input())

print('escreva mais um nome: ')
nome = input()


    
if nome in nomes:
    print('Achei')
else:
    print('não achei')    
'''

'''
2) Escreva um algoritmo que permita a leitura das notas de uma turma de 20 alunos. Calcular a média da turma e contar quantos alunos obtiveram nota acima desta média calculada. Escrever a média da turma e o resultado da contagem.

nota = 0
lista = []
media = 0
soma = 0
qtd_alunos = 0

for i in range (0, 3, 1):
    print('Digite a nota do aluno')
    nota = float(input())
    lista.append(nota)

for n in lista:
    soma = soma + n

media = soma / 3

for n in lista:
    if n > media:
        qtd_alunos += 1

print('e a media dos alunos em {}, {} alunos obtiveram media maior que a media'.format(media, qtd_alunos))
'''
'''
3) Ler um vetor Q de 20 posições (aceitar somente números positivos). Escrever a seguir o valor do maior elemento de Q e a respectiva posição que ele ocupa no vetor.
'''
'''
vetor = []
valor = 0
indicemaior = 0


for i in range (0, 3, 1):
    print('Escreva o valor')
    valor = int(input())
    vetor.append(valor)
    while valor < 0:
        print('valor negativo, escreva o valor:')
        valor = int(input())
    
    for i in range (len(vetor)):
        if vetor[i] == max(vetor):
            indicemaior = i 



print('o maior elemento é o {}, e ocupa a posição Nº{}.'.format(max(vetor), indicemaior + 1))        
'''
'''
4) O mesmo exercício anterior, mas agora deve escrever o menor elemento do vetor e a respectiva posição dele nesse vetor

vetor = []
valor = 0
indicemaior = 0


for i in range (0, 3, 1):
    print('Escreva o valor')
    valor = int(input())
    vetor.append(valor)
    while valor < 0:
        print('valor negativo, escreva o valor:')
        valor = int(input())
    
    for i in range (len(vetor)):
        if vetor[i] == min(vetor):
            indicemaior = i 



print('o menor elemento é o {}, e ocupa a posição Nº{}.'.format(min(vetor), indicemaior + 1)) 
'''
'''
5)Ler um vetor A de 10 números. Após, ler mais um número e guardar em uma variável X. Armazenar em um vetor M o resultado de cada elemento de A multiplicado pelo valor X. Logo após, imprimir o vetor M.
'''
'''
vetora = []
num = 0
varx = 0
vetorm = []

for i in range (0, 10, 1):
    print('Digite um numero')
    num = int(input())
    vetora.append(num)

print('Escreva mais um numero:')
varx = int(input())

for n in range (len(vetora)):
    vetorm.append(vetora[n] * varx)

print(vetorm)       
'''
'''
6)Faça um algoritmo para ler 20 números e armazenar em um vetor. Após a leitura total dos 20 números, o algoritmo deve escrever esses 20 números lidos na ordem inversa.
'''
'''
vetor = []
numero = 0

for i in range (0, 5, 1):
    print('Digite um numero')
    numero = int(input())
    vetor.append(numero)

for x in reversed(vetor):
    print(x)
'''
'''
7)Faça um algoritmo para ler um valor N qualquer (que será o tamanho dos vetores). Após, ler dois vetores A e B (de tamanho N cada um) e depois armazenar em um terceiro vetor Soma a soma dos elementos do vetor A com os do vetor B (respeitando as mesmas posições) e escrever o vetor Soma.
'''
'''
tam_vetor = int(input('Digite o tamanho do vetor: '))
valoresa = 0
valoresb = 0
vetora = []
vetorb = []
vetor_soma = []
soma = 0

for i in range (0, tam_vetor, 1):
    print('Digite os valores do vetor a: ')
    valoresa = int(input())
    vetora.append(valoresa)
    
for i in range (0, tam_vetor, 1):
    print('Digite os valores do vetor b: ')
    valoresb = int(input())
    vetorb.append(valoresb)
        
for i in range (len(vetora)):
    vetor_soma.append(vetora[i] + vetorb[i])

print(vetor_soma)

'''
'''
8)Faça um algoritmo para ler e armazenar em um vetor a temperatura média de todos os dias do ano 😊. Calcular e escrever: 
a)	Menor temperatura do ano 
b)	Maior temperatura do ano 
c)	Temperatura média anual 
d)	O número de dias no ano em que a temperatura foi inferior à média anual
'''
'''
vetor_temp = []
temp = 0
media = 0
soma = 0
inf = 0

for i in range (0, 5, 1):
    print('Escreva a temperatura: ')
    temp = float(input())
    vetor_temp.append(temp)

for n in vetor_temp:
    soma = soma + n
    

media = soma / 5

for n in vetor_temp:
    if n < media:
        inf += 1

print('A menor temperatura é: {}, a maior temperatura é: {}, a temperatura média é: {}, o numero de dias que a temperatura foi inferior a média é de: {}'.format(min(vetor_temp), max(vetor_temp), media, inf))
'''
'''
9)Faça um algoritmo para ler 10 números e armazenar em um vetor. Após isto, o algoritmo deve ordenar os números no vetor em ordem crescente. Escrever o vetor ordenado.
'''
'''
vetor = []
num = 0
for i in range(0, 10, 1):
    print ('Digite um valor: ')
    num = int(input())
    vetor.append(num)

numordenados = sorted(vetor)
print(numordenados)    
'''
'''

10)O mesmo exercício anterior, mas depois de ordenar os elementos do vetor em ordem crescente, deve ser lido mais um número qualquer e inserir esse novo número na posição correta, ou seja, mantendo a ordem crescente do vetor.
'''
'''
vetor = []
num = 0
numplus = []
num2 = 0

for i in range(0, 10, 1):
    print ('Digite um valor: ')
    num = int(input())
    vetor.append(num)

print('Digite mais um numero: ')
num2 = int(input())
numplus.append(num2)
vetor = vetor + numplus

numordenados = sorted(vetor)
print(numordenados)  
'''
'''
11)Faça um algoritmo para ler um vetor de 20 números. Após isto, deverá ser lido mais um número qualquer e verificar se esse número existe no vetor ou não. Se existir, o algoritmo deve gerar um novo vetor sem esse número. (Considere que não haverá números repetidos no vetor).
'''
'''
vetor = []
num = 0
vetorn = []
num2 = 0
vet = []

for i in range(0, 20, 1):
    print('Digite um numero ')
    num = int(input())
    vetor.append(num)

print('Digite mais um numero: ')
num2 = int(input())
vetorn.append(num2)

if num2 in vetor:
    vet = vetor
    vet.remove(num2)
    print(vet)
else:
    print('não existe')    

'''
'''
12)Faça um algoritmo para ler dois vetores V1 e V2 de 15 números cada. Calcular e escrever a quantidade de vezes que V1 e V2 possuem os mesmos números e nas mesmas posições.
'''
'''

v1 = []
v2 = []
num = 0
num2 = 0
p = 0

for i in range (0, 3, 1):
    print('Digite os numeros de v1: ')
    num = int(input())
    v1.append(num)
    
for i in range (0, 3, 1):
    print('digite os numeros de v2: ')
    num2 = int(input())
    v2.append(num2)

for n in range(len(v1)):
    if v1[n] == v2[n]:
        p += 1

print(p)
'''
'''
13) Faça um algoritmo para ler um vetor de 30 números. Após isto, ler mais um número qualquer, calcular e escrever quantas vezes esse número aparece no vetor. 
'''
'''

vetor = []
num = 0
numex = 0
p = 0

for i in range (0, 5, 1):
    print('Escreva os numeros: ')
    num = int(input())
    vetor.append(num)

print('Digite mais um numero: ')
numex = int(input())

for n in range (len(vetor)):
    if vetor[n] == numex:
        p += 1

print(p)        

'''
'''

13) Faça um algoritmo para ler 50 números e armazenar em um vetor VET, verificar e escrever se existem números repetidos no vetor VET e em que posições se encotrnam.
'''
'''
vet = []
num = 0
vet2 = []
vet3 =[]
p = 0
vetp = []

for i in range(0, 5):
    print('Escreva os numeros: ')
    num = int(input())
    vet.append(num)

for n in range (0, len(vet)):
    for j in range (n + 1, len(vet)):
        if vet[n] == vet[j]:
            vet3 = vet[n]
            p += 1
            vetp.append('{} e {} repetem.'.format(n, j))

print('as posições de repetição {}'.format(p))
for i in range(0, len(vetp)):
    print ('Os numeros que se repetem {}'.format(vetp[i]))
'''
'''
notas = []

[7.0, 5.0, 9.0]  joão
[6.3, 5.0, 9.0]  maria
[8.0, 8.5, 9.2]  ana

print(notas[0][2])

notas_joão = [7.0, 5.0, 9.0, 8.0, 7.2, 5.3]
for i in range(0, len(notas_joão)):
    print(notas_joão[i])


#print todas as notas de um aluno
for i in range(0, len(notas)):
    for j in range(0, 3):
        print('notas[{}][{}] = {} '.format(i, j, notas[i][j]))


notas = []
qtd_alunos = int(input('Quantidade de alunos: '))
qtd_notas_aluno = int(input('Quantidade de notas por aluno: '))

#estrutura para formar uma lista
for i in range(0, qtd_alunos):
    notas_aluno = []
    notas.append(notas_aluno)
    for j in range(0, qtd_notas_aluno):
        nota = float(input('digite a nota do aluno {}'.format(i)))
        notas_aluno.append(nota)
    
'''
'''
almir vende frutas na sua barraca na feira
e com sucesso do ultimo ano ele planeja criar
preços diferentes para alta e baixa temporada
a sua ideia é que cada fruta tenha 2 preços: alta temporada e baixa temporada
crie um algoritmo que permita a almir cadastrar os preços de cada uma
das suas frutas e em seguida imprima a sistagem de preços cadastrada por ele. considere que almir vende 3 frutas em sua barraca: laranja goiaba e banana.
'''

precos = []

for i in range (0, 3):
    precosf = []
    precos.append(precosf)
    for j in range (0, 2):
        prec = float(input('Digite o preço da fruta {} '.format(i + 1)))
        precosf.append(prec)

for i in range(0, len(precos)):
    for j in range(0, 2):
        print('{}, preço {} = {} '.format(i + 1, j + 1, precos[i][j]))        













     









