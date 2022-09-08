# 5. Escreva uma classe “Quadrado”, crie dois métodos que retornem a área do quadrado e o perímetro, não crie a instância nesse exercício.

class Quadrado:
    
    def __init__(self, lado):
        self.lado = lado
    
    def area(self):
        return f'A área do quadrado é: {self.lado*self.lado}'
    
    def perimetro(self):
        return f'O perímetro do quadrado é {self.lado*4}'