# 3. Escreva uma classe “PessoaJurica” e herde Pessoa, agora
# modificando o comportamento, retorne o cnpj. Crie uma instância e acesse os dados

class Pessoa:
    
    def __init__(self, cpf):
        self.cpf = cpf
        
    def tipo_pessoa(self):
        return f'Pessoa física de CPF {self.cpf}'
    
class Pessoajuridica(Pessoa):
    
    def __init__(self, cpf, cnpj):
        self.cnpj = cnpj
        super().__init__(cpf)
        
    def tipo_pessoa(self):
        return f'Pessoa juridica de CNPJ {self.cnpj}'
      
pessoa_fisica = Pessoa('66666666')
pessoa_juridica = Pessoajuridica('', '77777777777777')

print(pessoa_fisica.tipo_pessoa())
print(pessoa_juridica.tipo_pessoa())