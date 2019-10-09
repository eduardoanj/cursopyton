class Veiculo:
    def __init__(self, pneus, pintura, marca, modelo):
        self.pneus = pneus
        self.pintura = pintura
        self.marca = marca
        self.modelo = modelo

    def __str__(self):
        return f'{self.pneus}, {self.pintura}, {self.marca}, {self.modelo}'  