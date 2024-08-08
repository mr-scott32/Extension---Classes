# Define a class for a Player character
class Player():
    # Initialize the Player with name, race, class, attack power, and health
    def __init__(self, name, race, cls, atk, health):
        self.name = name      # Store the player's name
        self.race = race      # Store the player's race (e.g., human, elf, etc.)
        self.cls = cls        # Store the player's class (e.g., warrior, mage, etc.)
        self.atk = atk        # Store the player's attack power
        self.health = health  # Store the player's health points

# Define a class for a Weapon
class Weapon():
    # Initialize the Weapon with a name, type of weapon, and damage
    def __init__(self, name, wpn, dmg):
        self.name = name      # Store the weapon's name
        self.wpn = wpn        # Store the type of weapon (e.g., sword, bow, etc.)
        self.dmg = dmg        # Store the weapon's damage

# Define a class for an Enemy character
class Enemy():
    # Initialize the Enemy with name, type, damage, and health
    def __init__(self, name, type, dmg, health):
        self.name = name      # Store the enemy's name
        self.type = type      # Store the enemy's type (e.g., orc, dragon, etc.)
        self.dmg = dmg        # Store the enemy's damage
        self.health = health  # Store the enemy's health points

