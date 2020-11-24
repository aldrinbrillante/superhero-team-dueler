from ability import Ability
from random import randint

##############################################################
# Weapon (Ability)
##############################################################
class Weapon(Ability):
    def attack(self):
        """
        returns a random value between one half to the full attack power of the weapon.
        """
        # TODO: Use integer division to find half of the max_damage value
        # then return a random integer between half of max_damage and max_damage
        attack_dmg = randint(int(self.max_damage)//2,int(self.max_damage))
        return attack_dmg
        