listeFruit = [] 
n = int(input("combien de fruit voulez vous entrer? "))
for i in range(n): 
    fruits = input("entrer vos fruit prefere: ")
    listeFruit.append(fruits)
for i in listeFruit:
    c=''
    while c!=listeFruit:
          c=input("choisir un de vos fruit preferer: ")
    print("Felicitation!!")        
