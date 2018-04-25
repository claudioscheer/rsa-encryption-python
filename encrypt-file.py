import sys

from Crypto import Random
from Crypto.Cipher import AES
from Crypto.PublicKey import RSA


key_file = sys.argv[1]
input_file = sys.argv[2]
output_file = input_file + ".enc"

aes_key = Random.new().read(16)
iv = Random.new().read(16)

aes = AES.new(aes_key, AES.MODE_CFB, iv)

with open(key_file, "r") as f:
    key = RSA.importKey(f.read())

file_to_encrypt = open(input_file, "rb")
file_encrypted = open(output_file, "wb")

aes_key_encrypted, = key.encrypt(aes_key, 0)
file_encrypted.write(aes_key_encrypted)
file_encrypted.write(iv)

m = file_to_encrypt.read(16)
while m:
    c = aes.encrypt(m)
    file_encrypted.write(c)
    m = file_to_encrypt.read(16)

file_encrypted.close()
file_to_encrypt.close()