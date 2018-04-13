from bloque import *
from KeyExpansion import *

class AES:
	def __init__(self, expanded_key):
		self.expanded_key = expanded_key
		self.bloque_dim = 4

	def AddRoundKey(self, bloque, round):
		key_byte_counter = 0
		for j in range(self.bloque_dim):
			for i in range(self.bloque_dim):
				bloque.set_at(i, j, bloque.at(i,j) ^ self.expanded_key[16*round + key_byte_counter])
				key_byte_counter += 1
		return bloque

	def SubByte(self, bloque):
		for j in range(self.bloque_dim):
			for i in range(self.bloque_dim):
				hex_word = f'{bloque.at(i,j):02x}'
            	bloque.set_at(i, j, (sbox[int(hex_word[0], 16)][int(hex_word[1], 16)]))
        return bloque

    def ShiftRows(self, bloque):
    	pass

    def MixColumns(self, bloque):
    	pass

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