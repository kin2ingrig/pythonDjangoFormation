##challenge1
# number = int(input("votre nombre: "))
# taille = int(input("entrer la taille: "))
# liste = []

# for i in range(1,taille+1):  
#     liste.append(i*number)
# print(liste)    
   
   
##challenge2

mot = input("entrer un mot: ")
# m=[]
# for i in mot:
#     m.append(i)
# print(m)  
m=""
for i in mot:
    if i not in m:
        m += i
print(f"{mot}")
print(f"nouvel valeur {m}")
        
