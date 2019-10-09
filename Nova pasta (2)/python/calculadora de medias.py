#calculadora de medias

print('calculadora de media simples')
print('qual a quantidade de numeros que voce deseja calcular a media?')
qtdnum = int(input())

soma_num = 0
for i in range (0, qtdnum):
    print('Digite o {}º numero'.format(i + 1))
    num = float(input())
    soma_num = soma_num + num

media = soma_num / qtdnum
print('Média: {:.2f}'.format(media))
