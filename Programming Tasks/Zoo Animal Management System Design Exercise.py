class Animal:

    zoo_name = "Natioanal Zoo"

    def __init__(self , name , species , age , sound):
        self.name = name
        self.species = species
        self.age = age
        self.sound = sound

    def make_sound(self):
        print(f"{self.name} says {self.sound}")

    def info(self):
        print(f"Name: {self.name}")
        print(f"Species: {self.species}")
        print(f"Age: {self.age}")
        print(f"Sound: {self.sound}")
        print(f"Zoo: {Animal.zoo_name}")

    def __str__(self):
        return f"{self.name} ({self.species}) ,Age:{self.age} , sound : {self.sound}"

class Bird(Animal):
    def __init__(self, name, species, age, sound , wing_span):
        super().__init__(name, species, age, sound)
        self.wing_span = wing_span
    
    def make_sound(self):
        print(f"{self.name} chrisps:{self.sound}")

    
lion = Animal("simba" , "Lion" , 5 , "Roar")
print(lion)
