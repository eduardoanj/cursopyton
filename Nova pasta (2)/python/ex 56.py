#O mesmo exercício anterior, mas agora não será informado o número de mercadorias em estoque. Então o funcionamento deverá ser da seguinte forma: ler o valor da mercadoria e perguntar ‘MAIS MERCADORIAS (S/N)?’. Ao final, imprimir o valor total em estoque e a média de valor das mercadorias em estoque.

valmerc = 0
merc = input('Quer digitar uma mercadoria? (s/n) ')
valmerc2 = 0
media = 0
val = 0
merc2 = 0
while (merc == 's') or (merc == 'S'):
    print('Digite o valor da mercadoria: ')
    valmerc = float(input())
    valmerc2 = valmerc2 + valmerc
    val = val + 1
    media = valmerc2 / val
    merc = input('Mais Mercadorias? (s/n)')
    if (merc == 'n') or (merc == 'N'):
        print('O valor total de estoque é: {}, e a média de valor é: {}'.format(valmerc2, media))
 
