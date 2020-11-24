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
    ''' Reset all heroes health to starting_health'''
    # TODO: for each hero in self.heroes,
    # set the hero's current_health to their starting_health
    pass


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
##############################################################
# Add heropip3 install pytest
##############################################################
    def add_hero(self, hero):
        '''Add Hero object to self.heroes.'''
        self.heroes.append(hero) 
