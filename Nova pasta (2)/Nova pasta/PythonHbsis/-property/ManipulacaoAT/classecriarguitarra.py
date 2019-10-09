class Guitarra:
    def __init__(self, cordas, tarrachas, captador):
        self.__cordas = cordas
        self.__tarrachas = tarrachas
        self.__captador = captador
#@property puxa os valores da classe.
#@... .setter, seta novo valor para a classe.    
    @property
    def cordas(self):
        return self.__cordas
#set não precisa return, o get precisa    
    def set_tarrachas(self, tarrachas):
        self.__tarrachas = tarrachas

    def get_tarrachas(self):
        return self.__tarrachas


guitarra = Guitarra('Daddario', 'gottoh', 'dimarzio')
guitarra.set_tarrachas('jumbo')


print(guitarra.cordas)
print(guitarra.get_tarrachas())