import random

class Armor:

    def __init__(self, name, max_block):
        # TODO: Create instance variables for the values passed in.
        self.name = name
        self.max_block = max_block

    # Build the block method for the Armor class
    def block(self):
        random_def = random.randint(0, self.max_block)
        return random_def


if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    armor = Armor("Debugging Shield", 10)
    print(armor.name)
    print(armor.block())