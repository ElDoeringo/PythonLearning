#Funktion 1:
def strenge(strl, str2): 
    print(strl + "\n" + str2)

strenge("Thomas", "Doering")
    #"\n" betyder linieskift

#Funktion 2:
def ligeTal(tal):
    if tal % 2 == 0: # % modolooperator dividerer tallet
        print("Ja") 
    else:
        print("Nej")

ligeTal(34)


#Funktion 3:
def oploeftI4(tal):
    print(tal * tal * tal * tal)

oploeftI4(2)

#Funktion 3a
def oploeftI4(tal):
    x = tal * tal 
    print("oploeft i 2", x)
    x *= tal
    print("oploeft i 3", x)
    x *= tal
    print("oploeft i 4", x)
    return x #Giver det samlede resultat for regnestykket

y = oploeftI4(5)
print(y)

