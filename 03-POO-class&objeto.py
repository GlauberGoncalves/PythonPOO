class Smartphone():
    def __init__(self):
        self.modelo = {}
        self.marca = {}
        self.atributos = {}

    def mostrar(self):
    	print("O modelo é o %s da marca %s e seu hardware contem %s" %(self.modelo, self.marca, self.atributos))

j5 = Smartphone()
j5.modelo = 'g5-540'
j5.marca = 'Samsung'
j5.atributos = ['display 5','camera 8MP','cor branca']

j5.mostrar()