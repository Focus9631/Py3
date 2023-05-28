from random import randint

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

alpha1={}
with open("dict.txt") as f:
    for line in f:
        key, value = line.split()
        alpha1[key] = int(value)
word=input('Шифруемое слово: ').lower()
w=[]
for let in word:
    w.append(alpha1[let])
while len(w)%3!=0:
    w.append(randint(33,36))
print(w)
code=input('Ключ: ').lower()
coder=[]
for let in code:
    coder.append(alpha1[let])
if len(coder)>9:
    print('Error: Длина ключа более 9 символов')
    raise SystemExit
while len(coder)%9!=0:
    coder.append(randint(33,36))
print(coder)
alpha2={v:k for k, v in alpha1.items()}
k1=[coder[0],coder[1],coder[2]]
k2=[coder[3],coder[4],coder[5]]
k3=[coder[6],coder[7],coder[8]]
w1=[w[0],w[1],w[2]]
w2=[w[3],w[4],w[5]]
enc11=(w1[0]*k1[0]+w1[1]*k2[0]+w1[2]*k3[0])%len(alpha1)
enc12=(w1[0]*k1[1]+w1[1]*k2[1]+w1[2]*k3[1])%len(alpha1)
enc13=(w1[0]*k1[2]+w1[1]*k2[2]+w1[2]*k3[2])%len(alpha1)
enc1=[enc11,enc12,enc13]
enc21=(w2[0]*k1[0]+w2[1]*k2[0]+w2[2]*k3[0])%len(alpha1)
enc22=(w2[0]*k1[1]+w2[1]*k2[1]+w2[2]*k3[1])%len(alpha1)
enc23=(w2[0]*k1[2]+w2[1]*k2[2]+w2[2]*k3[2])%len(alpha1)
enc2=[enc21,enc22,enc23]
##enc=[enc11,enc12,enc13,enc21,enc22,enc23]
##print(enc)
encw=[]
for i in enc1:
    encw.append(alpha2[i])
for i in enc2:
    encw.append(alpha2[i])
print('Зашифрованное слово: ', ''.join(encw))
det=(k1[0]*(k2[1]*k3[2]-k2[2]*k3[1])-1*k1[1]*(k2[0]*k3[2]-k2[2]*k3[0])+k1[2]*(k2[0]*k3[1]-k2[1]*k3[0]))%len(alpha1)
det1=modinv(det, len(alpha1))
ad11=(k2[1]*k3[2]-k2[2]*k3[1])%len(alpha1)
ad12=(-1*(k2[0]*k3[2]-k2[2]*k3[0]))%len(alpha1)
ad13=(k2[0]*k3[1]-k2[1]*k3[0])%len(alpha1)
ad21=(-1*(k1[1]*k3[2]-k1[2]*k3[1]))%len(alpha1)
ad22=(k1[0]*k3[2]-k1[2]*k3[0])%len(alpha1)
ad23=(-1*(k1[0]*k3[1]-k1[1]*k3[0]))%len(alpha1)
ad31=(k1[1]*k2[2]-k1[2]*k2[1])%len(alpha1)
ad32=(-1*(k1[0]*k2[2]-k1[2]*k2[0]))%len(alpha1)
ad33=(k1[0]*k2[1]-k1[1]*k2[0])%len(alpha1)
at1=[ad11,ad21,ad31]
at2=[ad12,ad22,ad32]
at3=[ad13,ad23,ad33]
inc=-1
for i in at1:
    e=(i*det1)%len(alpha1)
    inc+=1
    at1[inc]=e
inc=-1
for i in at2:
    e=(i*det1)%len(alpha1)
    inc+=1
    at2[inc]=e
inc=-1
for i in at3:
    e=(i*det1)%len(alpha1)
    inc+=1
    at3[inc]=e
dec=[(enc1[0]*at1[0]+enc1[1]*at2[0]+enc1[2]*at3[0])%len(alpha1),
     (enc1[0]*at1[1]+enc1[1]*at2[1]+enc1[2]*at3[1])%len(alpha1),
     (enc1[0]*at1[2]+enc1[1]*at2[2]+enc1[2]*at3[2])%len(alpha1),
     (enc2[0]*at1[0]+enc2[1]*at2[0]+enc2[2]*at3[0])%len(alpha1),
     (enc2[0]*at1[1]+enc2[1]*at2[1]+enc2[2]*at3[1])%len(alpha1),
     (enc2[0]*at1[2]+enc2[1]*at2[2]+enc2[2]*at3[2])%len(alpha1)]
print(dec)
decw=[]
for i in dec:
    decw.append(alpha2[i])
print('Дешифрованное слово: ', ''.join(decw))


