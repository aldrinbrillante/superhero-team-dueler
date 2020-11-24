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
        total_armor = 0
        for armor in self.armors:
            total_armor += armor.block()
  

##############################################################
# Fight
##############################################################
    def fight(self, opponent):
        winner = random.choice([self.name, opponent.name])
        print(f'{winner} has won the fight!')

##############################################################
# Is Alive Method
##############################################################
    def is_alive(self):
        '''
        Return True or False depending on whether the hero is alive or not.

        TODO: Check the current_health of the hero.
        if it is <= 0, then return False. Otherwise, they still have health
        and are therefore alive, so return True
        '''
        if self.current_health > 0:
            return True
        else:
            return False

##############################################################
# Take Damage
##############################################################
    def take_damage(self, damage):
        '''
        Updates self.current_health to reflect the damage minus the defense.

        TODO: Create a method that updates self.current_health to the current
        minus the the amount returned from calling self.defend(damage).
        '''
        self.current_health -= damage
        # self.current_health -= self.defend(damage)
        return self.current_health


            
##############################################################
# Debugging / Testing
##############################################################
if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    hero1 = Hero("Wonder Woman")
    hero2 = Hero("Dumbledore")
    #hero1.fight(hero2)

    my_hero = Hero("Grace Hopper", 200)
    # print(my_hero.name)
    # print(my_hero.current_health)

    ability = Ability("Great Debugging", 50)
    another_ability = Ability("Smarty Pants", 90)
    hero = Hero("Grace Hopper", 200)
    hero.add_ability(ability)
    hero.add_ability(another_ability)
    #print(hero.attack())

    hero = Hero("Grace Hopper", 200)
    shield = Armor("Shield", 50)
    hero.add_armor(shield)
    hero.take_damage(50)
    #print(hero.current_health)

    hero = Hero("Grace Hopper", 200)
    hero.take_damage(150)
    print(hero.is_alive())
    hero.take_damage(15000)
    print(hero.is_alive())

    