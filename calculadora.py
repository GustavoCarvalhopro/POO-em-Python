class Calculadora:
    def __init__(self, num1 , num2) -> None:
        self.valor_a = num1
        self.valor_b = num2
        
    def soma(self):
        return self.valor_a + self.valor_b

    def subtracao(self):
        return self.valor_a - self.valor_b    

    def divisao(self):
        return self.valor_a / self.valor_b    


    def multiplicacao(self):
        return self.valor_a * self.valor_b    



calculador = Calculadora(10 , 2)

print(calculador.soma())
print(calculador.subtracao())
print(calculador.divisao())
print(calculador.multiplicacao())