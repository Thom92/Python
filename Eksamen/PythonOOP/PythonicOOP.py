
#Class definition, constructors and children classes
class Dog:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def description(self):
        return "{} is {} years old".format(self.name, self.age)
    def speak(self, sound):
        return "{} says {}".format(self.name, sound)
class RussellTerrier(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)
class Bulldog(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)

#Properties getter & setter
class P:
    def __init__(self, x):
        self.x = x        
    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, x):
        self._x = x        

#*args: accepts any positional arguments and creates a tuple. Can be used on any iterable that Python provides
#**Kwargs: accepts keywords. Can only be used on dictionaries
def my_function(a, b, *args, **kwargs):
    pass
my_first_dict = {"A": 1, "B": 2}
my_second_dict = {"C": 3, "D": 4}
my_merged_dict = {**my_first_dict, **my_second_dict} 
print(my_merged_dict)

