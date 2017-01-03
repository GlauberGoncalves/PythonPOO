# Primeira aula de orientação a objetos

class Caneta():
    modelo = {}
    cor = {}
    ponta = {}
    carga = {}
    tampada = {}

    def rabiscar():
        if(Caneta.tampada == True):
            print('Erro. Não posso rabiscar')
        else:
            print('Estou rabiscando')

    def tampar(): Caneta.tampada = True
    def destampar(): Caneta.tampada = False

c1 = Caneta
c1.cor = "preta"
c1.ponta = 0.5
c1.tampada = False

c2 = Caneta
c2.cor = 'Azul'
c2.tampada = True

c1.tampar()
c2.destampar()

c1.rabiscar()
c2.rabiscar()
