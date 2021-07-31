from ellipticcurve.ecdsa import Ecdsa
from ellipticcurve.privateKey import PrivateKey
import os

privateKey = PrivateKey()
pubKey = privateKey.publicKey()


message = 'Hello ECDSA!'
sign = Ecdsa.sign(message, privateKey)
isVerify = Ecdsa.verify(message, sign, pubKey)

outStr = 'Message: \n' + message + '\n\n'
outStr += 'Signature (base64): \n' + sign.toBase64() + '\n\n'
outStr += 'Public key: \n' + pubKey.toPem() + '\n\n'
outStr += 'Private key: \n' + privateKey.toPem() + '\n\n'
outStr += 'Verify message: ' + str(isVerify) + '\n'

resF = open('out.txt', 'w')
resF.write(outStr)
resF.close()
os.system('cat ./out.txt')
