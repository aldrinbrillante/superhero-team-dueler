# class for dog.py
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        print("dog initialized!")

my_dog = Dog("Rex", 'superdog')
# Adding the "breed" property on the fly
print(my_dog.breed)