

'''lista_op = []

opz = 3

def entra_menu():
    print('0 - Sair')
    print('1 - Cadastrar')
    print('2 - listar alunos')
    global opz  
    opz = int(input('Escreva uma opção'))
    

def entra_dados():
    nome = str(input('Qual o seu nome? '))
    sobrenome = str(input('Qual o seu sobrenome? '))
    idade = int(input('Qual a sua idade? '))
    cpf = str(input('Qual o cpf? '))
    pessoa = Pessoas(nome, sobrenome, idade, cpf)
    return lista_op.append(pessoa)

while opz != 0:
    entra_menu()
    if opz == 1:
        entra_dados()
    elif opz == 2:
        for i in lista_op:
            print(i)    
        
   
for i in lista_op:
    print(i)'''
    


    



'''nome = 'Angus'
sobrenome = 'Young'
                      #a é um append, w escreve, r lê, x só cria o arquivo
arquivo = open('gl.txt','a')
arquivo.write('Eduardo dos anjos')'''