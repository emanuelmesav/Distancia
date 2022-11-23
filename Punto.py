import math

class Punto:
    def __init__(self):
        self.x=0
        self.y=0
        

    def calcular_distancia(self,otroPunto ):


        a=(self.x-otroPunto.x)
        b=(self.y-otroPunto.y)
        
        r=math.sqrt(math.pow(a,2) + math.pow(b,2))
        return r