#Metoder er funktioner inden for en klasse
#Funktioner der er specifikke til en klasse 
# def funktionNavn(self, para1, para2):
        #Gør noget

#_init_
# - Initialize
        # Det første/starter noget
        # Sætter variabler
        # self
# def_init_(self, para1, para2):
        #self.para1 = para1
        #self.para2 = para2
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
        """En metode for at få dyr til at sige "noget"""
        if self.species == "dog":
            print("bark")
        else:
            print("I am not a dog!")

    @classmethod
    def animalFromString(cls, aniString):
                species, race, gender = aniString.split('-')
                return cls(species, race, gender)
 
Fido = Animal("dog", "boston terrier", "male")
Misser = Animal("cat", "norsk skovkat", "female")
newHorse = "horse-icelandic-female"
Epona = Animal.animalFromString(newHorse)

print(Epona.present)


print(Fido.__doc__)
Fido.speak()
print(Fido.speak.__doc__)

