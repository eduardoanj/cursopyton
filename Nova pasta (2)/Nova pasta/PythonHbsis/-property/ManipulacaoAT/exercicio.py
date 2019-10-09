lista = []
opcao = 3

class Cadastro:
    def __init__(self, nome, sobrenome, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf
    
    def __str__(self):
        return (f'O nome do aluno é: {self.nome} {self.sobrenome} O cpf é: {self.cpf}')

def cadastro():
    print('Cadastro de alunos')
    nome = str(input('Digite o nome do aluno: '))
    sobrenome = str(input('Digite o sobrenome do aluno: '))
    cpf = str(input('Digite o cpf do aluno: '))
    cadastro = Cadastro(nome, sobrenome, cpf)
    lista.append(cadastro)
#matriz fazemos for dentro de for, para salvar informações dentro de informação
while opcao != 1:
    print('0 - Cadastro')
    print('1 - Sair')
    print('2 - listar')
    opcao = int(input())

    if opcao == 0:
        cadastro()    

    if opcao == 2:
        for i in lista:
            print(i)
        #for i in lista e o print(i) no caso de classes serve para imprimir o def__srt__ da classe, no caso onde eu posso imprimir e editar.    