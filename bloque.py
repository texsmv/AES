import numpy as np
from funciones import *

class bloque:
    def __init__(self, text):
        self.texto = completar(text_to_int(text))

    def at(self,b, i, j):
        return self.texto[b * 16 + j * 4 + i]

    def imprimir_bloque(self, b):
        for i in range(0, 4):
            print(self.at(b, i,0), self.at(b, i,1), self.at(b, i,2), self.at(b, i,3))



a = bloque("hola")
a.imprimir_bloque(0)
