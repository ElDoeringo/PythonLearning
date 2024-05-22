#Def en løkke itererer over kode ved en betingelse
A = [1,2,3,4]
B = [1,2,3,4]
sum = 1

for i in range(len(A)):
    sum *= A[i]
print(sum)

def plusLister(liste1, liste2): #listerne 1 & 2 bliver til en ny liste i linie 10 
    #Resultat liste
    C = []
    #Vi iterer over hvert element i listerne
    for i in range(len(liste1)):
        #Vi lægger elementet vi iterer over sammen, og ligger det ind i C
        C.append(liste1[i] + liste2[i])
    print(C)
plusLister(A, B) #listerne 1 0g 2 bliver lagt sammen linerne 2+3
print(A+B)
