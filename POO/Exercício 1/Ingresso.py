class Ingresso:

    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor 
    
    def exibir_valor(self):   
        print(self.valor)
    
    def __str__(self):
        print(f"O nome do evento é {self.nome} e o valor do ingresso é R$ {self.valor:.2f}")