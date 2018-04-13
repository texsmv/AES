from AES import *

class Encriptador:
    def __init__(self, key):
        self.encrypted_text = ''
        self.key = key
        key_expansion = AESKeyExpansion(key)
        key_expansion.RunGen()
        self.expanded_key = key_expansion.GetExpandedKey()
        
        self.AES_encrypter = AES(self.expanded_key)

    def SetEncryptedText(self, encrypted_text):
        self.encrypted_text = encrypted_text

    def Run(self, text):
        block_list = Bloques(text)
        for b in block_list.bloques:
            self.AES_encrypter.RunRounds(b)
        encrypted_text = block_list.get_text()
        self.SetEncryptedText(encrypted_text)
        return encrypted_text

    def GetEncryptedText(self):
        return self.encrypted_text
