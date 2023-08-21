class Robot_Dog:
    # constructor used to initialize properties/state like name, breed, hungry
    # self is first parameter and refers to the object itself. "this"
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    # methods of a class are functions with 'self' as the first parameter.
    def back(self):
        print('Woof Woof!')
# Main program

my_dog = Robot_Dog('Spot', 'Chihuaha')
print(my_dog.name)
print(my_dog.breed)