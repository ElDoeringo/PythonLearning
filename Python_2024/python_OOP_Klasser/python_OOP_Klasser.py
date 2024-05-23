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
        self.race = race
        self.gender = gender
      
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
                    #KLASSER#
#Def - en klasse er en samling af attributter og funktioner omkring et koncept
        #Hvad/hvorfor - opgave
        # - Lav din egen datatype
        # - Hvert element af en datatype har flere attributter til fælles

        #class KLasseNavn
        # Evt. forklaring på klasse
        #GlobalKlasseAttribu0 = 0
        #GlobalKlasseAttribu0 = 1

        #def_inmit_(self, Lokalattribut1, Lokalattribut2)
                #self.Lokalattribut1 = Lokalattribut1
                  #self.Lokalattribut2 = Lokalattribut2
        #def funktion(self):
                #GlobalKlasseAttribut0++
                #prinmt(GlobalKlasseAttribut0)