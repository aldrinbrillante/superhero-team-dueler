import random
from ability import Ability
from armor import Armor

class Hero:
    # We want our hero to have a default "starting_health",
    # so we can set that in the function header.
    def __init__(self, name, starting_health=100):
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.abilities = list()
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
    
    def add_ability(self, ability):
        ''' Add ability to abilities list '''
        # We use the append method to add ability objects to our list.
        self.abilities.append(ability)

    def fight(self, opponent):
        winner = random.choice([self.name, opponent.name])
        print(f'{winner} has won the fight!')
            

if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    hero1 = Hero("Wonder Woman")
    hero2 = Hero("Dumbledore")
    # hero1.fight(hero2)

    my_hero = Hero("Grace Hopper", 200)
    # print(my_hero.name)
    # print(my_hero.current_health)

    ability = Ability("Great Debugging", 50)
    hero = Hero("Grace Hopper", 200)
    hero.add_ability(ability)
    print(hero.abilities)

    