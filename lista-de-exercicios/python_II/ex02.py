# 2. Escreva uma classe “PessoaFisica” e herde Pessoa, crie um método
# exclusivo para a classe e acesse-o

class Pessoa:
    
    def __init__(self, cpf, nome, idade, fumante):
        self.cpf = cpf 
        self.nome = nome 
        self.idade = idade 
        self.fumante = fumante

class PessoaFisica(Pessoa):
    
    def __init__(self, cpf, nome, idade, fumante, cidade):
        self.cidade = cidade
        super().__init__(cpf, nome, idade, fumante) 
        
    def dados(self):
        if self.fumante == "F":
            return f'{self.nome} CPF: {self.cpf}, Cidade: {self.cidade}, Idade: {self.idade}, é fumante'
        
        if self.fumante == "N":
            return f'{self.nome} CPF: {self.cpf} Cidade: {self.cidade}, Idade: {self.idade}, não é fumante'
        
pessoa1 = PessoaFisica('44444444', 'Marcela', '25', 'F', 'São Paulo')
pessoa2 = PessoaFisica('55555555', 'Ana', '21', 'N', 'Sorocaba')

print(pessoa1.dados())
print(pessoa2.dados()) 