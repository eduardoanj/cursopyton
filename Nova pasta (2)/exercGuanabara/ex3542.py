lado1 = float(input('Digite o primeiro lado: '))
lado2 = float(input('Digite o segundo lado: '))
lado3 = float(input('Digite o terceiro lado: '))

if ((lado1 + lado2) <= lado3):
    print('não forma um triangulo!!')
else:
    if ((lado2 + lado3) <= lado1):
       print('não forma um triangulo!!')
    else:
        if ((lado3 +lado1) <= lado2):
            print('não forma triangulo!!')
        else:
            if lado1 == lado2 == lado3:
                print('Forma um triângulo equilátero')
            elif lado1 == lado2 and lado2 != lado3:
                print('Forma um triângulo isóceles') 
            elif lado2 == lado3 and lado3 != lado1:
                print('Forma um triângulo isóceles')
            elif lado3 == lado1 and lado1 != lado2:
                print('Forma um triângulo isóceles')
            elif lado1 != lado2 and lado2 != lado3 and lado3 != lado1:
                print('É um triângulo escaleno')    
