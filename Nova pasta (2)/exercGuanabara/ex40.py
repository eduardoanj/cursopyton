nota1 = float(input('Digite o nome do aluno: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1+nota2)/2

if media >= 7:
    print('Aprovado!!')
elif media < 5:
    print('Reprovado!!')  
elif media < 6.7 and media >=5:
    print('Recuperação')      
