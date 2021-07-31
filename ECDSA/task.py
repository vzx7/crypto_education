from ellipticcurve.ecdsa import Ecdsa
from ellipticcurve.privateKey import PrivateKey
import os

privateKey = PrivateKey()
pubKey = privateKey.publicKey()

message = 'Hello ECDSA!'
sign = Ecdsa.sign(message, privateKey)


resF = open('out.txt', 'w')
resF.write('Message: \n' + message + '\n\n')
resF.write('Signature (base64): \n' + sign.toBase64() + '\n\n')
resF.write('Public key: \n' + pubKey.toPem() + '\n\n')

resF.write('Private key: \n' + privateKey.toPem() + '\n\n')

resF.close()
os.system('cat ./out.txt')
