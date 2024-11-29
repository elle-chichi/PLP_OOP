# create a class representing the superhero Thor, add attributes and methods, use constructors to initialize objects with unique values
class Superhero:
    def __init__(self, name, fatherName, power, hairColor):
        self.name = name
        self.fatherName = fatherName
        self.power = power
        self.hairColor = hairColor

    def display_identity(self):
        return f"My name is {self.name}, but I go by the name 'Son of {self.fatherName}'!"

    def display_power(self):
        return f"The strength I am know for in the galaxy is {self.power}!"
 
    def display_hairColor(self):
        return f"The color of my my hair is {self.hairColor}."

    def my_dad_favorite_sayings(self):
        return f"{self.fatherName}'s favorite saying was 'Let no man glory in the greatness of his mind'!"

# Inheritance example (subclass)

class AngryThor(Superhero):
    def __init__(self, name, fatherName, power, hairColor, anger_aggregate):
        super().__init__(name, fatherName, power, hairColor)
        self.anger_aggregate = anger_aggregate

    def display_anger_aggregate(self):
        return f"I get really angry when {self.anger_aggregate} by my enemies!"

    # Overriding the my_dad_favorite_sayings
    def my_dad_favorite_sayings(self):
        return f"{self.fatherName} always came to my rescue when I was in doubt with {self.power} and battling {self.anger_aggregate}"


# creating a Superhero object for Thor
Thor = Superhero("Thor", "Odison", "control over lightning", "blond")
print(Thor.display_identity())
print(Thor.display_power())
print(Thor.display_hairColor())
print(Thor.my_dad_favorite_sayings())

# creating an AngryThor object
AngryThor = AngryThor("Thor", "Odison", "control over lightning", "blond", "attack on my community")
print(AngryThor.display_identity)
print(AngryThor.display_power)
print(AngryThor.display_hairColor)
print(AngryThor.my_dad_favorite_sayings)
print(AngryThor.display_anger_aggregate)
