#Opsamling video 6
import random as rand

Sten = "Sten"
Saks = "Saks"
Papir = "Papir"

ditValg = input("Sten, Saks eller Papir?\n")            
PCvalg = rand.randint(1,3)  

if ditValg == Sten: #her vælger man sten
    if PCvalg == 1:
        print("I valgte begge Sten")
    elif PCvalg == 2:
        print("Du vandt, Sten vinder over Saks")
    else:
        print("Du tabte, Sten taber til papir")
                
elif ditValg == Saks:#her vælger man saks
    if PCvalg == 1:
        print("Du tabte, Sten vinder over Saks")
    elif PCvalg == 2:
        print("I valgte begge Saks")
    else:
        print("Du vinder, Saks vinder over Papir") 


elif ditValg == Papir:#her vælger man papir               
    if PCvalg == 1:
        print("Du vinder, Papir vinder over Sten")
    elif PCvalg == 2:
        print("Du taber, Saks vinder over papir")
    else:
        print("I valgte begge Papir")            
       
else:          
     print("Du skal huske at skrive med stort")           
                
                
                
                
                
                
                
                
                
                
                
                
