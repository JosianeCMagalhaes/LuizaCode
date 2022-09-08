# 4. Crie um professor de classe com atributos nome, idade e salário, onde
# o salário deve ter um método privado que não pode ser acessado fora
# da classe.
# a. Crie um método para acessar o método privado, onde é passada
# a identificação do usuário se ele pode ou não acessar.

class Professor:
    
    def __init__(self, nome, idade, cargo, salario):
        self.nome = nome
        self.idade = idade
        self.cargo = cargo
        self.salario = salario
        
    def __buscasalario(self):
        return f'O salário do professor {self.nome} é de: {self.salario}'
        
    def userconsulta(self, cargo):
        if cargo == 'Diretor':
            return self.__buscasalario()
            
professor1 = Professor('Junior', '26', 'Professor', 'R$ 7000.00').userconsulta('Diretor')

print(professor1)