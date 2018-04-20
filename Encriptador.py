from AES import *

class Encriptador:
    def __init__(self, key):
        self.encrypted_text = ''
        self.decrypted_text = ''
        self.key = key
        key_expansion = AESKeyExpansion(key)
        key_expansion.RunGen()
        self.expanded_key = key_expansion.GetExpandedKey()

        self.AES_encrypter = AES(self.expanded_key)

    def SetEncryptedText(self, encrypted_text):
        self.encrypted_text = encrypted_text

    def SetDecryptedText(self, decrypted_text):
        self.decrypted_text = decrypted_text

    def Run(self, text, encryption_bool):
        block_list = Bloques(text)

        output_text = ''
        if encryption_bool:
            for b in block_list.bloques:
                print(b.mat)
                self.AES_encrypter.RunRounds(b, 1)
            output_text = block_list.get_text()
            self.SetEncryptedText(output_text)
        else:
            for b in block_list.bloques:
               self.AES_encrypter.RunRounds(b, 0)
            output_text = block_list.get_text()
            self.SetDecryptedText(output_text)
        return output_text

    def GetEncryptedText(self):
        return self.encrypted_text

    def GetDecryptedText(self):
        return self.decrypted_text
