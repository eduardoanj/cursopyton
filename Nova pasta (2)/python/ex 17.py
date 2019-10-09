horainicio = int(input('Digite a hora de inicio (1-24): '))
horafim = int(input('Digite a hora do fim (1-24): '))

if (horafim < horainicio):
    resultado = ((24-horainicio) + horafim)
else:
    resultado = (horainicio + horafim)  

print('O jogo durou {}'. format(resultado))


