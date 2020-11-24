import random
from ability import Ability
from armor import Armor
from weapon import Weapon

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
        self.deaths = 0
        self.kills = 0
        
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
# Add death
##############################################################  
    def add_death(self, num_deaths):
        ''' Update deaths with num_deaths'''
        self.deaths += num_deaths

##############################################################
# Add kill
############################################################## 
    def add_kill(self, num_kills):
        """Update self.kills by num_kills amount"""
        self.kills += num_kills

##############################################################
# Add weapon
##############################################################   
    def add_weapon(self, weapon):
        '''Add weapon to self.abilities'''
        # TODO: This method will append the weapon object passed in as an
        # argument to self.abilities.
        # This means that self.abilities will be a list of
        # abilities and weapons.
        self.abilities.append(weapon)

##############################################################
# Attack
##############################################################
    def attack(self):
      # start total = 0
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
        '''
        Current Hero will take turns fighting the opponent hero passed in.
        '''
        # TODO: Fight each hero until a victor emerges.
        # Phases to implement:
        # 0) check if at least one hero has abilities. If no hero has abilities, print "Draw"
        if len(self.abilities) == 0 and len(opponent.abilities) == 0:
                print("Draw")
        # 1) else, start the fighting loop until a hero has won
        else:
        # 2) the hero (self) and their opponent must attack each other and each must take damage from the other's attack
            while self.is_alive() == True and opponent.is_alive() == True:
                self.take_damage(opponent.attack())
                opponent.take_damage(self.attack())
            # 3) After each attack, check if either the hero (self) or the opponent is alive
            # 4) if one of them has died, print "HeroName won!" replacing HeroName with the name of the hero, and end the fight loop
            if self.is_alive() == False:
                opponent.add_kill(1)
                self.add_death(1)
                print(f"{opponent.name} has killed {self.name}. {opponent.name} has won.")
            elif opponent.is_alive() == False:
                self.add_kill(1)
                opponent.add_death(1)
                print(f"{self.name} has killed {opponent.name}. {self.name} has won.")
        

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
    #print(hero.is_alive())
    hero.take_damage(15000)
    #print(hero.is_alive())

    hero1 = Hero("Wonder Woman")
    hero2 = Hero("Dumbledore")
    ability1 = Ability("Super Speed", 300)
    ability2 = Ability("Super Eyes", 130)
    ability3 = Ability("Wizard Wand", 80)
    ability4 = Ability("Wizard Beard", 20)
    hero1.add_ability(ability1)
    hero1.add_ability(ability2)
    hero2.add_ability(ability3)
    hero2.add_ability(ability4)
    hero1.fight(hero2)

    hero = Hero("Wonder Woman")
    weapon = Weapon("Lasso of Truth", 90)
    hero.add_weapon(weapon)
    print(hero.attack())

    