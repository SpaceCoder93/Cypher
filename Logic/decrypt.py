from Crypto.Cipher import AES
from base64 import b64decode
import hashlib

class Decrypt:
    def __init__(self, enc_dict, password):
        salt = b64decode(enc_dict['salt'])
        cipher_text = b64decode(enc_dict['cipher_text'])
        nonce = b64decode(enc_dict['nonce'])
        private_key = hashlib.scrypt(
            password.encode(), salt=salt, n=2**14, r=8, p=1, dklen=32)
        cipher = AES.new(private_key, AES.MODE_GCM, nonce=nonce)
        decrypted = self.unpad(cipher.decrypt(cipher_text))
        return decrypted.decode('utf-8')

    def unpad(self, data):
        return data[:-data[-1]]