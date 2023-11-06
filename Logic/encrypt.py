from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from base64 import b64encode
import hashlib

class Encrypt:
    def encrypt(self, plain_text, password):
        salt = get_random_bytes(AES.block_size)
        private_key = hashlib.scrypt(
            password.encode(), salt=salt, n=2**14, r=8, p=1, dklen=32)
        cipher_config = AES.new(private_key, AES.MODE_GCM)
        cipher_text, tag = cipher_config.encrypt_and_digest(self.pad(plain_text.encode('utf-8')))
        return {
            'cipher_text': b64encode(cipher_text).decode('utf-8'),
            'salt': b64encode(salt).decode('utf-8'),
            'nonce': b64encode(cipher_config.nonce).decode('utf-8')
        }
    def pad(self, data):
        length = 16 - (len(data) % 16)
        return data + bytes([length] * length)