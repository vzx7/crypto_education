from Crypto.Random import get_random_bytes
from Crypto.Protocol.SecretSharing import Shamir
from Crypto.Cipher import AES
import os

key = get_random_bytes(16)
cipher = AES.new(key, AES.MODE_EAX)
ciphertext, tag = cipher.encrypt_and_digest(bytearray(b'hello world!'))
shares = Shamir.split(2, 5, key)

s1 = shares[0]
s2 = shares[3]


file_out = open("encrypted.bin", "wb")
[file_out.write(x) for x in (s1[1], s2[1], cipher.nonce, tag, ciphertext)]
file_out.close()


file_in = open("encrypted.bin", "rb")
s11, s22, nonce, tag, ciphertext = [
    file_in.read(x) for x in (16, 16, 16, 16, -1)]


keyChek = Shamir.combine([(1, s11), (4, s22)])

# let's assume that the key is somehow available again
cipher = AES.new(keyChek, AES.MODE_EAX, nonce)
data = cipher.decrypt_and_verify(ciphertext, tag)
print(data.decode('utf-8'))

#os.system('cat ./encrypted.bin')
