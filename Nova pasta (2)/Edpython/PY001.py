print('='*60)


'''
1. Leia uma frase digitada pelo usuário.
2. Leia uma letra digitada pelo usuário.
3. Informe para o usuário quantas vezes aparece na frase (passo 1) a letra (passo 2).
4. Informe para o usuário a posição em que a letra aparece a primeira vez na frase.
5. Informe para o usuário a posição em que a letra aparece pela última vez na frase.
'''

frase = str(input('{}Digite uma frase: '.format(''*5)))
letra = str(input('{}Digite uma letra: '.format(''*5)))
#############################################################ao invés de find(buscar) pode ser index(vetor)
print('{}A letra digitada aparece {}, vezes na frase'.format(''*5, frase.count(letra)))
print('{}A primeira letra {},apareceu na posição {}'.format(''*5, letra, frase.index(letra)))
print('{}A ultima letra {} apareceu na posição {}'.format(''*5, letra, frase.rindex(letra)))
''
######### o *60 é para repetir 60 vezes a string
print('='*60)