from cryptography.fernet import Fernet
import base64

class Crypt():


    def __init__(self):
        """
        Generates a new key when this class gets called
        """
        self.key = Fernet.generate_key()


    def encrypt(self, s):
        """
        Takes a message in bytes or str format and encrypts it
        Returns message encrypted
        """
        f = Fernet(self.key)
        token = f.encrypt(s)
        return token


    def decrypt(self, key, token):
        """
        Takes a key and message to decrypt
        Returns the decrypted message
        """
        bytes_object = base64.urlsafe_b64decode(key)
        f = Fernet(bytes_object)
        result = f.decrypt(token)
        return result
