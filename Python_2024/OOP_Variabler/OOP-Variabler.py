#               Variabler      #
#To typer
    #Klasse variabler
        #Globalt
        #Nødvendighed
    #Objekt variabler
        #Lokalt
        #Primær
# class KlasseNavn:
    #Definition af klasse (globale) variabler
        #DetKanVæreInt = 0 altså tal
        #DetKanVæreString = "eksempel mit navn er"
        #DetKanVæreLister = [1, 2, 3, 4, 5, "Ting"]

#Definition af Objekt (lokale) variabler
    #def_init_(self, Lokal1, Lokal2)
        #self.Lokal1 = lokal1
        #self.Lokal2 = Lokal2
class  Animal:
    """En klasse for konceptet dyr"""
    alive = "Yes"
    numAni = 0

    def __init__(self, species, race, gender):#objekt
        self.species = species
        self.race = race
        self.gender = gender
        self.present = "I am a " + species + " and my race is " + race + " and my gender is " + gender

        Animal.numAni+= 1

      
    def speak(self):
        if self.species == "dog":
            print("bark")
        else:
            print("I am not a dog!")

Fido = Animal("dog", "boston terrier", "male")
Misser = Animal("cat", "norsk skovkat", "female")
print(Animal.numAni)
print(Misser.present)
print(Misser.gender)