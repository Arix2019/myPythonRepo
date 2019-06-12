#
#
class ClassePessoa:

    def __init__(self, nome, sexo, idade=0):
        self.nome = nome
        self.sexo = sexo
        self.idade = idade

    def setNome(self, nome):
        return self.nome

    def setSeco(self, sexo):
        return self.sexo

    def setIdade(self, idade):
        return self.idade

    def getNome(self):
        return self.nome

    def getSexo(self):
        return self.sexo

    def getIdade(self):
        return self.idade


pessoa = ClassePessoa('Mel', 'Fêmea', 5)

print(pessoa.getIdade())

