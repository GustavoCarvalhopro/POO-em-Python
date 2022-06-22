class Televisao:
    def __init__(self):
        self.ligada = False

    def power(self):
        if self.ligada:
            self.ligada = False
        else:
            self.ligada = True    


televisao = Televisao()
print('A Televisão está ligada? {}'.format(televisao.ligada))   
televisao.power()
print('A Televisão está ligada? {}'.format(televisao.ligada))
televisao.power()
print('A Televisão está ligada? {}'.format(televisao.ligada))         

   