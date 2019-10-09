print('escreva a primeira e a segunda nota do aluno: ')
nota1 = int(input())
nota2 = int(input())

media = int((nota1 + nota2) / 2)

if (media < 6):
    print('A media do aluno é: {}, portanto ele está REPROVADO!!'. format(media))
else:
    print('A media do aluno é: {}, portanto ele está APROVADO!!'. format(media))    