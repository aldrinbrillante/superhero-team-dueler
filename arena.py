from ability import Ability
from weapon import Weapon
from armor import Armor
from hero import Hero
from team import Team

class Arena:
    def __init__(self):
        '''
            Instantiate properties
            team_one: None
            team_two: None
        '''
        self.team_one: None
        self.team_two: None
    
    def create_ability(self):
        name = input("What is the ability name?  ")
        max_damage = input("What is the max damage of the ability?  ")
        return Ability(name, max_damage)
    
    def create_armor(self):
        '''
            Prompt user for Armor information
            return Armor with values from user input.
        '''
        name = input("What is the name of your armor? ")
        damage_reduction = int(input("What is the max damage reduction of your armor? "))
        return Armor(name, damage_reduction)


    def create_weapon(self):
        '''
            Prompt user for Weapon information
            return Weapon with values from user input.
        '''
        name = input("What is your weapon's name?  ")
        max_damage = int(input("What is the max damage of your weapon? "))
        return Weapon(name, max_damage)
