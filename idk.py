import random
import math

p = 13
q = 23
n = p*q
phi_n = (p - 1) * (q - 1)

e = random.randint(2, phi_n - 1) #szedek egy random e-t
while math.gcd(e, phi_n) != 1:
    e = random.randint(2, phi_n - 1)


def Extended_Euclid(m,n): 
    A1,A2,A3 = 1,0,m
    B1,B2,B3 = 0,1,n
    while B3!=0:
        Q = A3//B3
        T1,T2,T3 = A1-Q*B1,A2-Q*B2,A3-Q*B3
        A1,A2,A3 = B1,B2,B3
        B1,B2,B3 = T1,T2,T3
        d=A1%n
    return d

def encrypt(M, public_key):
    return pow(M,public_key[0])% public_key[1]

def decrypt(CT, private_key):
    return pow(CT,private_key[0]) % private_key[1]

print("Példa feladat p=13,q=23,e=17,m=15")
e = 17
d = Extended_Euclid(e,phi_n)
m = 15
publickey = [e,n]
privatekey = [d,n]
print("üzenet:",m,"public kulcs:",publickey,"private kulcs:",privatekey)
print("titkositva:",encrypt(m,publickey))
print("visszafejtve:",decrypt(encrypt(m,publickey),privatekey))