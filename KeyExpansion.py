from funciones import *

class AESKeyExpansion:
    def __init__(self, key):
        self.key = key
        self.key_size = len(key)
        self.expanded_key = []

    def ConcatenateBytes(self, number_list):
        B = ''
        for i in number_list:
            B += format(i,'08b')
        return int(B, 2)

    def SeparateBytes(self, bin_number):
        return [int(bin_number[i:i+8],2) for i in range(0, len(bin_number), 8)]

    def K(self, offset):
        A = []
        for i in range(offset, offset+4):
            A.append(ord(self.key[i]))
        return A

    def EK(self, offset):
        A = []
        for i in range(offset, offset+4):
            A.append(self.expanded_key[i])
        return A

    def RotWord(self, word):
        A = word[:]
        A.append(A.pop(0))
        return A

    def SubWord(self, word):
        A = []
        for i in word:
            hex_word = format(i,'02x')
            A.append(sbox[int(hex_word[0], 16)][int(hex_word[1], 16)])
        return A

    def Rcon(self, Round):
        Rcon_values = ['01000000','02000000','04000000','08000000','10000000','20000000','40000000','80000000','1B000000','36000000','6C000000', 'D8000000', 'AB000000','4D000000','9A000000']
        R = int((Round/(self.key_size/4))-1)
        return int(Rcon_values[R], 16)

    def GenExpandedKey(self, Rounds, a, b):
        for r in range(0, Rounds):
            if r < a:
                self.expanded_key.extend(self.K(r*4))
            elif r%b == 0:
                self.expanded_key.extend(self.SeparateBytes(format(self.ConcatenateBytes(self.SubWord(self.RotWord(self.EK((r-1)*4)))) ^ self.Rcon(r) ^ self.ConcatenateBytes(self.EK((r-4)*4)), '032b')))
            else:
                self.expanded_key.extend(self.SeparateBytes(format(self.ConcatenateBytes(self.EK((r-1)*4)) ^ self.ConcatenateBytes(self.EK((r-4)*4)), '032b')))

    def RunGen(self):
        L = len(self.key)
        if L == 16:
            self.GenExpandedKey(44, 4, 4)
        elif L == 24:
            self.GenExpandedKey(52, 6, 6)
        elif L == 32:
            self.GenExpandedKey(60, 8, 4)

    def GetExpandedKey(self):
        return self.expanded_key
