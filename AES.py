from bloque import *
from KeyExpansion import *

class AES:
    def __init__(self, expanded_key):
        self.expanded_key = expanded_key
        self.bloque_dim = 4

    def AddRoundKey(self, bloque, round_num):
        key_byte_counter = 0
        for j in range(self.bloque_dim):
            for i in range(self.bloque_dim):
                bloque.set_at(i, j, bloque.at(i,j) ^ self.expanded_key[16*round_num + key_byte_counter])
                key_byte_counter += 1
        return bloque

    def SubByte(self, bloque):
        for j in range(self.bloque_dim):
            for i in range(self.bloque_dim):
                hex_word = f'{bloque.at(i,j):02x}'
                bloque.set_at(i, j, (sbox[int(hex_word[0], 16)][int(hex_word[1], 16)]))
        return bloque

    def ShiftRows(self, bloque):
        for i in range(1, 4):
            bloque.mat[i] = np.roll(bloque.mat[i], -i)
        return bloque

    def MixColumns(self,  bloque):
        for i in range(0, 4):
            bloque.set_at(0, i, mult(bloque.at( 0, i), 2) ^ mult(bloque.at( 1, i), 3) ^ mult(bloque.at( 2, i), 1) ^ mult(bloque.at(3, i), 1))
            bloque.set_at(1, i, mult(bloque.at( 0, i), 1) ^ mult(bloque.at( 1, i), 2) ^ mult(bloque.at( 2, i), 3) ^ mult(bloque.at(3, i), 1))
            bloque.set_at(2, i, mult(bloque.at( 0, i), 1) ^ mult(bloque.at( 1, i), 1) ^ mult(bloque.at( 2, i), 2) ^ mult(bloque.at(3, i), 3))
            bloque.set_at(3, i, mult(bloque.at( 0, i), 3) ^ mult(bloque.at( 1, i), 1) ^ mult(bloque.at( 2, i), 1) ^ mult(bloque.at(3, i), 2))
        return bloque

    def RunRounds(self, bloque):
        Rounds = 0
        if len(self.expanded_key) == 176:
            Rounds = 10
        elif len(self.expanded_key) == 208:
            Rounds = 12
        elif len(self.expanded_key) == 240:
            Rounds = 14
        self.AddRoundKey(bloque, 0)
        for R in range(1, Rounds+1):
            if R == Rounds:
                self.AddRoundKey(self.ShiftRows(self.SubByte(bloque)), R)
            else:
                self.AddRoundKey(self.MixColumns(self.ShiftRows(self.SubByte(bloque))), R)
