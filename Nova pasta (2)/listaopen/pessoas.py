class Pessoas:
    def __init__(self, nome, sobrenome, idade, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.cpf = cpf

    def __str__(self):
        return (f'{self.nome}, {self.sobrenome}, {self.idade}, {self.cpf}') 
