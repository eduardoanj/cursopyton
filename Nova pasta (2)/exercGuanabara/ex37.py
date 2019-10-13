num = int(input('Digite um numero inteiro: '))

base_original = int(input('A base original, 1 para binario, 2 para octa, e 3 para hexadecimal'))

if base_original ==1:
    print('O numero {} convertido para binário é {}'.format(num, bin(num)))
elif base_original ==2:
    print('O numero {} convertido para octal é {}'.format(num, oct(num)))
elif base_original ==3:
    print('O numero {}, convertido para hexadecimal é {}'. format(num, hex(num)))        
else:
    print('opção errada!!')    