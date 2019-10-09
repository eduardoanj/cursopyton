numconta = int(input('Digite o numero da conta: '))
credito = float(input('Digite o crédito: '))
debito = float(input('Digite o debito: '))
saldo = float(input('Digite o saldo: '))

saldoatual = (saldo - debito + credito)
#se a variavel está dentro do if ela pertence ao if, sempre declarar a variavel antes do if com o valor 0
# variavel = 0, caso ligue direto no if ela pode não existir caso voce a utilize fora;
if (saldoatual >= 0):
    print('Saldo Positivo ')
else:
    print('Saldo Negativo ')    
