class Team:

##############################################################
# __init__
##############################################################
    def __init__(self, name):
        '''
        Initialize your team with its team name and an empty list of heroes
        '''
        self.name = name
        self.heroes = list()
        
##############################################################
# Add hero
##############################################################
    def add_hero(self, hero):
        '''Add Hero object to self.heroes.'''
        self.heroes.append(hero)


##############################################################
# Attack
##############################################################
    def attack(self, other_team):
        ''' Battle each team against each other.'''
        living_heroes = list()
        living_opponents = list()

        for hero in self.heroes:
            living_heroes.append(hero)

        for hero in other_team.heroes:
            living_opponents.append(hero)

        while len(living_heroes) > 0 and len(living_opponents)> 0:
            # TODO: Complete the following steps:
            # 1) Randomly select a living hero from each team (hint: look up what random.choice does)
            random_hero = random.choice(living_heroes)
            random_opponent = random.choice(living_opponents)
            # 2) have the heroes fight each other (Hint: Use the fight method in the Hero class.)
            # 3) update the list of living_heroes and living_opponents
            # to reflect the result of the fight

##############################################################
# Remove Hero
##############################################################
    def remove_hero(self, name):
        '''
        Remove hero from heroes list. If Hero isn't found return 0.
        '''
        foundHero = False
        for hero in self.heroes:
            if hero.name == name:
                self.heroes.remove(hero)
                foundHero = True
        if not foundHero:
            return 0

##############################################################
# Revive Hero
##############################################################
    def revive_heroes(self, health=100):
        '''Reset all heroes health to starting_health'''
        # TODO: for each hero in self.heroes,
        # set the hero's current_health to their starting_health
        for hero in self.heroes:
            hero.current_health(health)


##############################################################
# Stats
##############################################################
    def stats(self):
        '''Print team statistics'''
        for hero in self.heroes:
            kd = hero.kills / hero.deaths
            print("{} Kill/Deaths:{}".format(hero.name,kd))
    
##############################################################
# View All Heroes
##############################################################
    def view_all_heroes(self):
        '''Prints out all heroes to the console.'''
        for hero in self.heroes:
            print(hero)
