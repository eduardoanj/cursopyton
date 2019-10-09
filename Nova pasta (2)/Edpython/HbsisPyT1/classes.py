
class Investimento:
    def __init__(self, categoria, tipo, aporte, rentabilidade, periodo_rentabilidade):
        self.categoria = categoria
        self.tipo = tipo
        self.aporte = aporte
        self.rentabilidade = rentabilidade
        self.periodo_rentabilidade = periodo_rentabilidade

class Carteira_investimento:
    def __init__(self, investimento, quantidade, rentabilidade_mensal, rentabilidade_anual):
        self.investimento = investimento
        self.quantidade = quantidade
        self.rentabilidade_mensal = rentabilidade_mensal
        self.rentabilidade_anual = rentabilidade_anual   
