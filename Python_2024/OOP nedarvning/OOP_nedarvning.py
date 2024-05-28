#Hvad er en klasse?
    #class KlasseNavn(SuperClass):
#"""Evt. forklarinmg på klasse"""
#GlobalKLasseAttribut0 = 0
#GlobalKLasseAttribut1 = 1
#def_init_(self, Lokalattribut1, Lokalattribut2)
        #self.Lokalattribut1 = Lokalattribut1
        #self.Lokalattribut1 = Lokalattribut1

#defc funktion(self)
   #GlobalKlasseAttribut0++
    #print(GlobalKlasseAttribut0)

                        #Nedarvning
# Hvornår skal det bruges?
# - Kat og hund?
# - hvad får jeg med?

class Animal:
    """En klasse for konceptet dyr"""
    alive = "Yes"
    numAni = 0

    def __init__(self, species, race, gender):
        self.species = species
        self.race = race
        self.gender = gender
        self.present = "I am a " + species + " and my race is " + race + " and my gender is " + gender
        Animal.numAni += 1

    def speak(self):
        """En metode for at få dyr til at sige noget"""
        print("I am an animal")

class Dog(Animal):
    """En klasse for arten hund"""
    numDog = 0

    def __init__(self, species, race, gender, owner):
        super().__init__(species, race, gender)  # Call the parent class's __init__ method
        self.owner = owner
        self.present = ("I am a {0} and my race is {1} and my owner is called {2}").format(self.species, self.race, self.owner)
        Dog.numDog += 1

    def speak(self):
        print("Bark!!")

    def play(self, thing):
        print(f"I play catch with a {thing}")

class Cat(Animal):
    """En klasse for arten hund"""
    numCat = 0

    def __init__(self, species, race, gender, owner):
        super().__init__(species, race, gender)  # Call the parent class's __init__ method
        self.owner = owner
        self.present = ("I am a {0} and my race is {1} and my owner is called {2}").format(self.species, self.race, self.owner)
        Cat.numCat += 1

    def speak(self):
        print("Miaw!!")

    def play(self, thing):
        print(f"I play catch the mouse {thing}")

# Create an instance of Dog
Fido = Dog("dog", "Boston Terrier", "male", "Bent Betjent")
print(Fido.present)  # Print the 'present' attribute of the Fido instance
Fido.speak()         # Call the 'speak' method
Fido.play("ball")    # Call the 'play' method with argument "ball"

# Create an instance of Cat
Misser = Cat("Cat", "Norsk skovkat", "male", "Børges bodega")
print(Misser.present)  # Print the 'present' attribute of the Misser instance
Misser.speak()         # Call the 'speak' method
Misser.play("with a laser pointer")    # Call the 'play' method with argument "laser pointer"
