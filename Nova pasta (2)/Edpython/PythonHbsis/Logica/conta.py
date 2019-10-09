numb ="Bradesco"

def cria_conta(nome, numero_conta, saldo):   
    return {'nome':nome, 'numero_c':numero_conta, 'saldo':saldo }

def depositar(cnt, valor):
    cnt['saldo'] += valor
    
def sacar(cnt,valor):
    cnt['saldo'] -= valor
#o medoto tem por objetivo definir funções onde terá uma sequencia de comandos, e quando você precisar dessas sequência em alguma parte do programa basta chama-la que ela vai executar a função que você definiu.

exp de função:

def print_soma(numero1, numero2):
print numero1 + numero2

print_soma(5, 6)
#aqui fiz uma praticamente inútil mas criar funções é exencial para fazer bons programas
#o comando global serve para a variavel indicada seja usada em qualquer metodo , no caso do metodod def imprime, será alterada a variavel original, fora do metodo.
def imprime():
    global numb
    print(numb)    
#def é um metodo, para chamar um metodo  é apenas colocar o nome dele mais os parenteses
imprime()
def altera():
    numb = numb+ 'amarelo'
    print(numb)    