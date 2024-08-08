from game_objects import Player, Weapon, Enemy
import random

# Create an instance of Player
player_character = Player('Gimli', 'Dwarf', 'Fighter', 3, 180)

# Create an instance of Weapon with random damage between 12 and 15
player_weapon  = Weapon("Balin's Axe", 'Greataxe', random.randint(12, 15))

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
