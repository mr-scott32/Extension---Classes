# Extension - Classes
This will show you an example of how we can setup a Player, Weapon and Enemy class. 

### Step 1: Create `game_objects.py`

In the `game_objects.py` file, define the classes `Player`, `Weapon`, and `Enemy`.

```python
# game_objects.py

class Player:
    def __init__(self, name, race, cls, atk, health):
        self.name = name      # Store the player's name
        self.race = race      # Store the player's race (e.g., human, elf, etc.)
        self.cls = cls        # Store the player's class (e.g., warrior, mage, etc.)
        self.atk = atk        # Store the player's attack power
        self.health = health  # Store the player's health points

class Weapon:
    def __init__(self, name, wpn, dmg):
        self.name = name      # Store the weapon's name
        self.wpn = wpn        # Store the type of weapon (e.g., sword, bow, etc.)
        self.dmg = dmg        # Store the weapon's damage

class Enemy:
    def __init__(self, name, type, dmg, health):
        self.name = name      # Store the enemy's name
        self.type = type      # Store the enemy's type (e.g., orc, dragon, etc.)
        self.dmg = dmg        # Store the enemy's damage
        self.health = health  # Store the enemy's health points
```

### Step 2: Create `show_stats.py`

In the `show_stats.py` file, import the classes from `game_objects.py`, create instances of `Player`, `Weapon`, and `Enemy`, and print their stats.

```python
# show_stats.py

from game_objects import Player, Weapon, Enemy
import random

# Create an instance of Player
player_character = Player('Gimli', 'Dwarf', 'Fighter', 3, 180)

# Create an instance of Weapon with random damage between 12 and 15
player_weapon = Weapon("Balin's Axe", 'Greataxe', random.randint(12, 15))

# Create an instance of Enemy with random damage between 15 and 18, and random health between 80 and 140
enemy_character = Enemy('Azog', 'Orc Warrior', random.randint(15, 18), random.randint(80, 140))

# Print the player character details
print(f"Player Name: {player_character.name}")
print(f"Player Race: {player_character.race}")
print(f"Player Class: {player_character.cls}")
print(f"Player Attack: {player_character.atk}")
print(f"Player Health: {player_character.health}")

# Print the player weapon details
print(f"Weapon Name: {player_weapon.name}")
print(f"Weapon Type: {player_weapon.wpn}")
print(f"Weapon Damage: {player_weapon.dmg}")

# Print the enemy character details
print(f"Enemy Name: {enemy_character.name}")
print(f"Enemy Type: {enemy_character.type}")
print(f"Enemy Damage: {enemy_character.dmg}")
print(f"Enemy Health: {enemy_character.health}")
```

### Step 3: Running the Code

1. Ensure both `game_objects.py` and `show_stats.py` are in the same directory.
2. Run the `show_stats.py` script to see the output.
