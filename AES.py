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

    def SubByte(self, bloque, encryption_bool=1):
        for j in range(self.bloque_dim):
            for i in range(self.bloque_dim):
                hex_word = format(bloque.at(i,j), '02x')

                if encryption_bool:
                    bloque.set_at(i, j, (sbox[int(hex_word[0], 16)][int(hex_word[1], 16)]))
                else:
                    bloque.set_at(i, j, (sbox_inverse[int(hex_word[0], 16)][int(hex_word[1], 16)]))
        return bloque

    def ShiftRows(self, bloque, encrypt):
        if encrypt:
            enc = 1
        else:
            enc = -1
        for i in range(1, 4):
            bloque.mat[i] = np.roll(bloque.mat[i], -i * enc)
        return bloque

    def MixColumns(self,  bloque, encrypt):
        m_enc = [[2,3,1,1],[1,2,3,1],[1,1,2,3],[3,1,1,2]]
        m_des = [[14,11,13,9],[9,14,11,13],[13,9,14,11],[11,13,9,14]]
        if encrypt:
            m = m_enc
        else:
            m = m_des
        for i in range(0, 4):
            b1 = bloque.at( 0, i)
            b2 = bloque.at( 1, i)
            b3 = bloque.at( 2, i)
            b4 = bloque.at( 3, i)


            bloque.set_at(0, i, mult(b1, m[0][0]) ^ mult(b2, m[0][1]) ^ mult(b3, m[0][2]) ^ mult(b4, m[0][3]))
            bloque.set_at(2, i, mult(b1, m[2][0]) ^ mult(b2, m[2][1]) ^ mult(b3, m[2][2]) ^ mult(b4, m[2][3]))
            bloque.set_at(3, i, mult(b1, m[3][0]) ^ mult(b2, m[3][1]) ^ mult(b3, m[3][2]) ^ mult(b4, m[3][3]))
            bloque.set_at(1, i, mult(b1, m[1][0]) ^ mult(b2, m[1][1]) ^ mult(b3, m[1][2]) ^ mult(b4, m[1][3]))



    def RunRounds(self, bloque, encryption_bool):
        Rounds = 0
        if len(self.expanded_key) == 176:
            Rounds = 10
        elif len(self.expanded_key) == 208:
            Rounds = 12
        elif len(self.expanded_key) == 240:
            Rounds = 14
        if encryption_bool:
            self.AddRoundKey(bloque, 0)
        else:
            self.AddRoundKey(bloque, Rounds)
        for R in range(1, Rounds+1):

            print(bloque.mat)
            if encryption_bool:
                if R == Rounds:
                    self.SubByte(bloque, 1)
                    self.ShiftRows(bloque, 1)

                    self.AddRoundKey(bloque, R)
                else:

                    self.SubByte(bloque, 1)
                    self.ShiftRows(bloque, 1)
                    self.MixColumns(bloque, 1)
                    self.AddRoundKey(bloque, R)

            else:
                if R == Rounds:
                    self.ShiftRows(bloque, 0)
                    self.SubByte(bloque, 0)
                    self.AddRoundKey(bloque, Rounds - R)


                else:
                    self.ShiftRows(bloque, 0)
                    self.SubByte(bloque, 0)
                    self.AddRoundKey(bloque, Rounds - R)
                    self.MixColumns(bloque, 0)
