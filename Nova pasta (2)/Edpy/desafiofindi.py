'''
Desafios teóricos:

1) Um sistema de controle de versão (como o próprio nome já diz) tem a finalidade de gerenciar 
diferentes versões de um documento. Com isso ele te oferece uma maneira muito mais inteligente e eficaz de organizar seu projeto,
 pois é possível acompanhar um histórico de desenvolvimento, desenvolver paralelamente e ainda te oferecer outras vantagens, como exemplo, 
 customizar uma versão, incluir outros requisitos, finalidades especificas, layout e afins sem mexer no projeto principal ou resgatar o 
 sistema em um ponto que estava estável, isso tudo sem mexer na versão principal.

 2) github = @eduardoanjos15 / edpy

'''
'''
Desafios teóricos:
'''
'''
1. Leia uma frase digitada pelo usuário.
2. Leia uma letra digitada pelo usuário.
3. Informe para o usuário quantas vezes aparece na frase (passo 1) a letra (passo 2).
4. Informe para o usuário a posição em que a letra aparece a primeira vez na frase.
5. Informe para o usuário a posição em que a letra aparece pela última vez na frase.
'''
'''
frase = str(input('Digite uma frase: ')).upper().strip()
letra = str(input('Digite uma letra: ')).upper().strip()

print('A letra digitada aparece {}, vezes na frase'.format(frase.count(letra)))
print('A primeira letra {},apareceu na posição {}'.format(letra, frase.find(letra)+1))
print('A ultima letra {} apareceu na posição {}'.format(letra, frase.rfind(letra)+1))
'''
'''
Criar um programa que utilize o método 50-20-10-20: 
1. Leia o salário líquido informado pelo usuário.
2. Organize os valores de acordo com o método citado.
3. Informe ao usuário qual o valor que ele deve destinar para 
cada categoria
'''
# Método 50-20-10-20 (50% gastos, 20% investimentos a longo prazo,
#  10% investimentos a curto prazo, 20% livre)
'''
salario = float(input('Digite o salário liquido '))

gastos = (salario / 100 * 50)
investimentos_lp = (salario / 100 * 20)
investimentos_cp = (salario / 100 * 10)
livre = (salario / 100 * 20)

print('O usuário deve usar R${} para gastos, R${} para investimentos a longo prazo, R${} para investimentos a curto prazo e sobram R${} livres. '.format(gastos, investimentos_lp, investimentos_cp, livre))
'''
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
    


