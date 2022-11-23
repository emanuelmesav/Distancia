from Punto import Punto


class Programa:
    def __init__(self):
        
        self.messi=Punto()
        self.elbicho=Punto()

        self.a=self.messi.calcular_distancia(self.elbicho)

        self.messi.x=8
        self.messi.y=2

        self.elbicho.x=9
        self.elbicho.y=9

        a=self.messi.calcular_distancia(self.elbicho)
        print(a)