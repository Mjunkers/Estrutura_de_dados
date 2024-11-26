class Ponto:

    def __init__(self, nome, eixo_x, eixo_y):
        self.nome = nome
        self.x = eixo_x
        self.y = eixo_y
    
    def __str__(self) -> str:
        return f"{self.nome}: {self.x}, {self.y}"
