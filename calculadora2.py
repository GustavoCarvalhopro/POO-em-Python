class Calculadora:
    def __init__(self) -> None:
       pass
        
    def soma(self, valor_a, valor_b):
        return valor_a + valor_b

    def subtracao(self, valor_a , valor_b):
        return valor_a - valor_b    

    def divisao(self, valor_a , valor_b):
        return valor_a / valor_b    


    def multiplicacao(self, valor_a, valor_b):
        return valor_a * valor_b    



calculador = Calculadora()

print(calculador.soma(3, 5))
print(calculador.subtracao(1215, 1235))
print(calculador.divisao(524, 3))
print(calculador.multiplicacao(12135, 300))