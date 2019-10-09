from veiculo import Veiculo

class Moto(Veiculo):
    def __init__(self, pneus, pintura, marca, modelo, guidon):
        super().__init__(pneus, pintura, marca, modelo)
        self.guidon = guidon

    def __str__(self):
        return f'{super().__str__()} - {self.guidon}'    