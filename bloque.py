import numpy as np
from funciones import *


class Bloque:
    def __init__(self, arreglo):
        self.mat = arreglo.reshape(4,4)
        self.mat = self.mat.transpose()

    def at(self,i, j):
        return self.mat[i][j]

    def set_at(self, i, j, val):
        self.mat[i][j] = val

class Bloques:
    def __init__(self, text):
        self.texto = completar(text_to_int(text))

        self.bloques = []
        for i in range(0, (int)(len(self.texto) / 16)):
            self.bloques  = self.bloques + [Bloque(self.texto[i*16 : (i + 1)*16])]





#a = bloque("hola")
#a.imprimir_bloque(0)
