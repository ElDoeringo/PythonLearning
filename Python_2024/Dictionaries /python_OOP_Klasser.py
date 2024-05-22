#Def = et paradigme er en mængde af konventioner
#Paradigme:
#   - en mængde af konventioner
#   - en måde at gøre tingene på
#   - regler for dit program 
#Def = et objekt er et stykke data med tilhørende attributter og operationer 
#           *Objekter
        # int - integer, heltal
        #   plus, minus
        # STR - STRING, streng
        #   plus, minus
        # dict.has_key(key)
#Def = en klasse er en samling af attributter og funktioner omkring et koncept
class  Animal:
    """En klasse for konceptet dyr"""
    alive = "Yes"

    def __init__(self, species, race, gender):
        self.species = species
        self.species = race
        self.species = gender
      
    def speak(self):
        if self.species == "dog":
            print("bark")
        else:
            print("I am not a dog!")

Fido = Animal("dog", "pug", "female")
print(Fido.alive)
print(Fido.species)
Fido.speak()
Fido.species ="cat"
print(Fido.species)
print(Fido.speak())
