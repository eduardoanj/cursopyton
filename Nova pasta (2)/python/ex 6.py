custofabrica = int(input('Digite o custo de fábrica do automovel: '))

valortotal = (custofabrica + (custofabrica / 100 * 28) + (custofabrica / 100 * 45))

print('O carro terá o valor de custo para o consumidor de: {}  '. format(valortotal))