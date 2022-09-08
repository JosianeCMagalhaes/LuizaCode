# 1. Dada as seguintes informações: Pessoa, cpf, nome e idade, crie uma
# classe onde teremos o retorno do documento, o retorno do nome e
# verificação de tipo de pessoa, onde um método irá receber como
# parâmetro “F” ou “N” para trazer fumante ou não fumante.
# Feito isso, crie uma instância e retorne esses valores.

class Pessoa:
    
    def __init__(self, cpf, nome, idade, fumante):
        self.cpf = cpf 
        self.nome = nome 
        self.idade = idade 
        self.fumante = fumante
    
    def fuma(self):
        if self.fumante == "F":
            return f'{self.nome} CPF: {self.cpf} Idade: {self.idade}, é fumante'
        
        if self.fumante == "N":
            return f'{self.nome} CPF: {self.cpf} Idade: {self.idade}, não é fumante'
    
pessoa1 = Pessoa("11111111", "Thais", "25", "N").fuma()
pessoa2 = Pessoa("22222222", "Renata", "28", "F").fuma()
pessoa3 = Pessoa("33333333", "Milene", "21", "N").fuma()

print(pessoa1)
print(pessoa2)
print(pessoa3)