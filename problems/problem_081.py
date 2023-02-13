# Write four classes that meet these requirements.
#
# Name:       Animal
#
# Required state:
#    * number_of_legs, the number of legs the animal has
#    * primary_color, the primary color of the animal
#
# Behavior:
#    * describe()       # Returns a string that describes that animal
#                         in the format
#                                self.__class__.__name__
#                                + " has "
#                                + str(self.number_of_legs)
#                                + " legs and is primarily "
#                                + self.primary_color
#
class Animal:
    def __init__(self, num_legs, primary_color):
        self.num_legs = num_legs
        self.primary_color = primary_color

    def describe(self):
        return self.__class__.__name__ + " has " + str(self.num_legs) + " legs and is primarily " + self.primary_color
#
# Name:       Dog, inherits from Animal
#
# Required state:       inherited from Animal
#
# Behavior:
#    * speak()          # Returns the string "Bark!"
#
class Dog(Animal):
    def __init__(self, primary_color):
        super().__init__(4, primary_color)
    def speak(self):
        return "Bark!"

#
# Name:       Cat, inherits from Animal
#
# Required state:       inherited from Animal
#
# Behavior:
#    * speak()          # Returns the string "Miao!"
#
class Cat(Animal):
    def __init__(self, primary_color):
        super().__init__(4, primary_color)
    def speak(self):
        return "Miao!"
#
# Name:       Snake, inherits from Animal
#
# Required state:       inherited from Animal
#
# Behavior:
#    * speak()          # Returns the string "Sssssss!"

class Snake(Animal):
    def __init__(self, primary_color):
        super().__init__(0, primary_color)
    def speak(self):
        return "Sssssss!"

animal_human = Animal(2, "tan")
dog_mimi = Dog("dark brown")
cat_Duke = Cat("tux")
snake_dotty = Snake("creamy")

print (animal_human.describe())
print (dog_mimi.describe())
print (dog_mimi.speak())
print (cat_Duke.describe())
print (cat_Duke.speak())
print (snake_dotty.describe())
print (snake_dotty.speak())