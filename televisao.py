class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 5

    def power(self):
        if self.ligada:
            self.ligada = False
        else:
            self.ligada = True    

    def aumenta_canal(self):
        if self.ligada == True:
            self.canal +=1    

    def diminui_canal(self):
        if self.ligada ==True:
            self.canal -=1            


televisao = Televisao()
print('A Televisão está ligada? {}'.format(televisao.ligada))   
televisao.power()
print('A Televisão está ligada? {}'.format(televisao.ligada))
televisao.power()
print('A Televisão está ligada? {}'.format(televisao.ligada))     
televisao.aumenta_canal() 
print(televisao.canal)
televisao.power()   
print('A Televisão está ligada: {}'.format(televisao.ligada))
televisao.aumenta_canal()
print(televisao.canal)
   