# 6. Crie um arquivo main.py, importe a classe “Quadrado”, crie uma nova instância e acesse seus métodos.

from ex05 import Quadrado

def main():
    quadrado = Quadrado(2)
    
    print(f'A área do quadrado é: {quadrado.area()}')
    print(f'O perímetro do quadrado é: {quadrado.perimetro()}')