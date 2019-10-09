numma = int(input('Digite o numero de maçãs: '))

if (numma > 12):
    num_menos = numma * 1.0
    print('O valor total da compra é de: {}'. format(num_menos))
else:
    num_menos = numma * 1.3
    print('O valor total da compra é de: {}'. format(num_menos))    