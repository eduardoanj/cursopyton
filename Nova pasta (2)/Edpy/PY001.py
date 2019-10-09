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