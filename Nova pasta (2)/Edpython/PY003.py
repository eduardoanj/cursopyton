'''
Criar um programa que:
1. Cadastre usuário e senha.
2. Liste usuários cadastrados e suas respectivas senhas.
3. Efetue login, validando usuário e senha.
Obs: O programa deve apresentar um menu para que o usuário possa realizar a ação que
desejar e no momento em que desejar.
'''

#nomes_guardados = [josé, pedro, maria]
#senhas_guardadas = [1234, 4321, 0000]
usuario = 0
senha = 0
a = 0
b = 0
c = 0

operacao = str(input('Deseja fazer uma operação? (s/n)'))


while (operacao != 'n') and (operacao != 's'):
    operacao = str(input('Caractere inválido, Deseja fazer uma operação? (s/n)'))
    if operacao.strip() == 's' or operacao.strip() == 'n':
        break

if operacao == 'n':
    print('Tenha um bom dia')

if operacao == 's':
    print('Escreva o usuario: ')
    usuario = str(input())
    print('Escreva a senha: ')
    senha = str(input())
    
    if usuario == 'josé' and senha == '1234':
        print('Login efetuado com sucesso!!')
        a = 1
    if usuario == 'pedro' and senha == '4321':
        print('Login efetuado com sucesso!!')
        b = 1  
    if usuario == 'maria' and senha == '0000':
        print('Login efetuado com sucesso!!')
        c = 1
    if (a == 0) or (b == 0) or (c == 0):
        print('Senha errada')     
    