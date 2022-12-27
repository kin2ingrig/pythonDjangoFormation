import random

cpt= random.randint(1, 100)
# print("le numeros est: ",cpt)

x= int(input("entrer un numero compris entre 1 et 100: "))
print(x)
if(x>100):
    print("votre numero est superieur a 100")
elif(x==cpt):
    print(x, "==", cpt, "Felicitation!!") 
elif(x>cpt):
    print(x, ">", cpt)       
elif(x<cpt):
    print(x, "<", cpt)   
        