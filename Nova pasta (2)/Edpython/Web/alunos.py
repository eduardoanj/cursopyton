class Alunos:
    #o self deve sempre ser adicionado quando está dentro de uma classe
    def __init__(self, nome, sobrenome, telefone):
        self.Nome = nome
        #adição da variavel sobrenome
        self.Sobrenome = sobrenome
        self.Telefone = telefone
    def nome_completo(self):
    #concatenação de strings tambem pode ser feita desta forma +''+
        nomecompleto = self.Nome +' '+ self.Sobrenome
        return nomecompleto    