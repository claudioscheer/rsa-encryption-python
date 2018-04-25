import sys

from Crypto import Random
from Crypto.Cipher import AES
from Crypto.PublicKey import RSA


key_file = sys.argv[1]
input_file = sys.argv[2]
output_file = input_file.split(".enc")[0]

with open(key_file, "r") as f:
    key = RSA.importKey(f.read())

file_to_decrypt = open(input_file, "rb")
file_decrypted = open(output_file, "wb")

aes_key = key.decrypt(file_to_decrypt.read(128))
iv = file_to_decrypt.read(16)

aes = AES.new(aes_key, AES.MODE_CFB, iv)

m = file_to_decrypt.read(16)
while m:
    c = aes.decrypt(m)
    file_decrypted.write(c)
    m = file_to_decrypt.read(16)

file_decrypted.close()
file_to_decrypt.close()