class Pessoa:
    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome=nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

    def comer(self, alimento):
        if self.comendo:
            print(f'{self.nome} já está comendo...')
            return


        print (f'{self.nome} está comendo {alimento}')
        self.comendo = True


    def parar_comer(self, alimento):
        if not self.comendo:
            print(f'{self.nome} não está comendo.')
            return

        print(f'{self.nome} parou de comer {alimento}.')
        self.comendo = False


            


    def falar(self, argumento):
        if self.comendo:
            print(f'{self.nome} não pode falar pois está comendo.')
            return
        print(f'{self.nome} está falando sobre {argumento}')
        self.falando = True    