import random

mot=input("entrer un mot: ")
m = []
for i in mot:
    m.append(i)
random.shuffle(m)
mot1 = ''
for i in m:
    mot1 += i
print(mot1)
