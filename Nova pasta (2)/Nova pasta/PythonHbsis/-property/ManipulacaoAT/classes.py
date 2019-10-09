class Veiculo:
    def __init__(self, pl, mc):
        self.__placa = pl
        self.marca = mc
        print('construtor da classe veiculo:{}'.format(self) )
    @property
    def placa(self):
        return self.__placa

class Carro(Veiculo):
    def __init__(self, cad, plc, mrc):       
        super().__init__(plc, mrc)
        self.cadeira = cad
   
class Moto(Veiculo):
    def __init__(self, plc, mrc, cld):
        super().__init__(plc, mrc)
        self.cilindrada = cld





print('='*50)
print('\n'*3)



carro = Carro(4, 'plc-1111', 'Honda')
moto = Moto('aaa-9999', 'Suzuki','1200cc')

print(carro.placa)
print(moto.cilindrada + ' - ' + moto.marca + ' - ' + moto.placa)




print('\n'*3)
print('='*50)