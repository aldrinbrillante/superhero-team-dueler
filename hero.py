import random
from ability import Ability
from armor import Armor

class Hero:
##############################################################
# __init__
############################################################## 
    def __init__(self, name, starting_health=100):
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.abilities = list()
        self.armors = list()
        
##############################################################
# Add ability
##############################################################
    def add_ability(self, ability):
        ''' Add ability to abilities list '''
        self.abilities.append(ability)
##############################################################
# Add armor
##############################################################   
    def add_armor(self, armor):
        self.armors.append(armor)

##############################################################
# Attack
##############################################################
    def attack(self):
      # start our total out at 0
      total_damage = 0
      # loop through all of our hero's abilities
      for ability in self.abilities:
          # add the damage of each attack to our running total
          total_damage += ability.attack()
          # return the total damage
          return total_damage
##############################################################
# Defend
##############################################################
    def defend(self):
        '''
        Calculate the total block amount from all armor blocks.
        return: total_block:Int
        
        This method should run the block method on each armor in self.armors
        '''
  

##############################################################
# Fight
##############################################################
    def fight(self, opponent):
        winner = random.choice([self.name, opponent.name])
        print(f'{winner} has won the fight!')
            
##############################################################
# Debugging / Testing
##############################################################
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
    another_ability = Ability("Smarty Pants", 90)
    hero = Hero("Grace Hopper", 200)
    hero.add_ability(ability)
    hero.add_ability(another_ability)
    print(hero.attack())

    