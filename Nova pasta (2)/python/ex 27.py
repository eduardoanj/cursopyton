print('Digite o primeiro, o segundo e o terceiro lado do triangulo: ')
ladoa = float(input())
ladob = float(input())
ladoc = float(input())

if ((ladoa + ladob) > ladoc) and ((ladob + ladoc) > ladoa) and ((ladoc+ladoa) > ladob):
    print('Os lados formam um triangulo')
else:
    print('Os lados não formam um triangulo')    