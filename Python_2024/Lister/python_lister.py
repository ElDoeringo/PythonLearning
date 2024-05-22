#Definition på en liste: en sekvens af datalementer
#EKSEMPEL liste = [elem0, elem1, elem2] - INDEXERE fra 0
A = [1,2,3,4,5]
print("Liste A")
print(A)

B = A + [1,5,79,6, "Thomas"] #Concatenate foregår i B = A + [......"...."]
print("Liste B")
print(B)

A.append(8)
print("Liste A")
print(A)

A.append([18,49])
print("Liste A")
print(A)

#[1, 2, 3, 4, 5, 8 [18, 49]] 6 element = [18,49]
print([18,49] [0])

C = 2 in A #betinget udtryk
print(C)

def findesI(liste, elem): #funktion
    if 2 in A:
        print("2 findes i A")
        print("elementet findes i listen")
    else:
        print("elementet findes ikke i listen")

findesI([2, 4,2, 8, 2], 5)