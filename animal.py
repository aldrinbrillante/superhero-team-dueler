class Animal():
    def __init__(self, name):
        self.name = name

    def eat(self):
        return f"{self.name} is eating"
    
    def drink(self):
        return f"{self.name} is drinking"


class Frog(Animal):
    def jump(self):
        print('{} is jumping'.format(self.name))