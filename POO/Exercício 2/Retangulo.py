class Retangulo:

    def __init__(self, altura, largura):
        self.altura = altura
        self.largura = largura

    def calcular_perimetro(self):
        perimetro = 2*self.altura + 2*self.largura
        print(f"O perimetro do retangulo é {perimetro:.2f}")

    def calcular_area(self):
        area = self.altura*self.largura
        print(f"A area do retangulo é {area:.2f}")