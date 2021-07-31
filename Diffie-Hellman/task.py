from tinyec.ec import SubGroup, Curve, Point

import secrets


def compress(key): return hex(key.x) + hex(key.y)[2:]


name = 'secp256k1'
p = 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffefffffc2f
n = 0xfffffffffffffffffffffffffffffffebaaedce6af48a03bbfd25e8cd0364141
a = 0x0000000000000000000000000000000000000000000000000000000000000000
b = 0x0000000000000000000000000000000000000000000000000000000000000007
g = (0x79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798,
     0x483ada7726a3c4655da4fbfc0e1108a8fd17b448a68554199c47d08ffb10d4b8)
h = 1
subGroup = SubGroup(p, g, n, h)
curve = Curve(a, b, subGroup, name)

alicePubKey_x = 14910571678862872761868841217294607909892752044215461914879649677693867889072
alicePubKey_y = 62514830396634191665984879881213930227864491048359651030093312396718750313589


myPrivKey = secrets.randbelow(curve.field.n)
myPubKey = myPrivKey * curve.g

pubKey = Point(curve, alicePubKey_x, alicePubKey_y)

mySharedKey = pubKey * myPrivKey
print('print sharedKey: ')
print(mySharedKey)
print()
print('compress sharedKey: ' + compress(mySharedKey))
