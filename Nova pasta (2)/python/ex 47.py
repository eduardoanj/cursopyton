#Ler 10 valores e escrever quantos desses valores lidos estão
#  no intervalo [10,20] (incluindo os valores 10 e 20 no intervalo)
#  e quantos deles estão fora deste intervalo.

dentro_intervalo = 0
fora_intervalo = 0 

for i in range(1, 11):
    print('Digite o valor {}'.format(i))
    num = int(input())
    if (num <= 20) and (num >= 10):
        dentro_intervalo += 1
    else:
        fora_intervalo += 1   
print('dentro do intervalo: {}, fora do intervalo: {}'.format(dentro_intervalo, fora_intervalo))         
