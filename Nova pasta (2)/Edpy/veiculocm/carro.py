from veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, pneus, pintura, marca, modelo, ar_condicionado):
        super().__init__(pneus, pintura, marca, modelo)
        self.ar_condicionado = ar_condicionado

    def __str__(self):
        return f'{super().__str__()} - {self.ar_condicionado}'    