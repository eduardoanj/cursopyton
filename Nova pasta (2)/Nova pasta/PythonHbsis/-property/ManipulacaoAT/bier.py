class Bier:
    def __init__(self, tipo, ibu, teor):
        self.__tipo = tipo
        self.__ibu = ibu
        self.__teor = teor
    
    def get_tipo(self):
        return self.__tipo

    def set_tipo(self, tipo):
        self.__tipo = tipo
#property faz o mesmo que o get mas no printar a variavel não precisa do get, basta setar a variavel em sí, isso tem por vantagem a pessoa que ver um codigo relativamente grande não consegue interpretar como uma função, e eu posso mexer no codigo primeiro e a pessoa que ver a area do print não vai saber.
#1 property e 1 setter por função, setter altera o valor dentro da classe.
###usar propriedade###
    @property
    def teor(self):
        return self.__teor
#@property precisa de (self) no metodo.
#@... .setter precisa de (self, nome) no metodo.

bier1 = Bier('ipa', 18, 12)
bier.set_tipo('weiss')


print('='*50)
print('\n'*3)

print(bier1.get_tipo())
print(bier.teor)