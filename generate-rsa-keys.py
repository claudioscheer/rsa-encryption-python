from Crypto.PublicKey import RSA


key = RSA.generate(1024)

with open("key.pem", "wb") as f:    
    f.write(key.exportKey("PEM"))

with open("public-key.pem", "wb") as f:    
    f.write(key.publickey().exportKey("PEM"))