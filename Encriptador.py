from AES import *

class Encriptador:
	def __init__(self, text, key):
		self.plain_text = text
		self.block_list = Bloques(text)
		self.encrypted_text = ''

		self.key = key
		key_expansion = AESKeyExpansion(key)
		key_expansion.RunGen()
		self.expanded_key = key_expansion.GetExpandedKey()

		self.AES_encrypter = AES(self.expanded_key)

	def SetEncryptedText(self):
		pass

	def Run(self):
		for b in self.block_list.bloques:
			self.AES_encrypter.RunRounds(b)
		self.SetEncryptedText()

	def GetEncryptedText(self):
		return self.encrypted_text
