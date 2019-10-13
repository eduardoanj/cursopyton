data = int(input('Digite a data de nascimento: '))

if data >= 2010:
    print('Mirim')
elif data < 2010 and data >= 2005:
    print('Infantil')
elif data < 2005 and data >= 2000:
    print('Junior')    
elif data < 2000 and data >= 1999:
    print('Sênior')
elif data < 1999:
    print('Master')    