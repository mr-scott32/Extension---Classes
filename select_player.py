from game_objects import Player, Weapon, Enemy  # Import the Player, Weapon, and Enemy classes from game_objects module
import random  # Import the random module to generate random numbers

# Create global variables to store the selected player and weapon
player = ''
weapon = ''

# Create a list of player characters
players = [Player('Gandalf', 'Human', 'Wizard', 2, 100),
           Player('Gimli', 'Dwarf', 'Fighter', 3, 180),
           Player('Legolas', 'Elf', 'Archer', 1, 120),
           Player('Aragorn', 'Human', 'Ranger', 4, 130)]

# Create a list of weapons with random damage values
weapons = [Weapon('Glamdring', 'Sword', random.randint(8, 12)),
           Weapon("Balin's Axe", 'Greataxe', random.randint(12, 15)),
           Weapon('Bow of the Galadhrim', 'Longbow', random.randint(10, 12)),
           Weapon('Anduril', 'Great Sword', random.randint(10, 14))]

# Function to select a player and their corresponding weapon
def selectPlayer():
    global player, weapon  # Use global variables to store the selected player and weapon
    player_selected = False  # Initialize a flag to track if a player has been selected
    while player_selected == False:  # Loop until a valid player is selected
        
        # try and except statements allow us to run code without fear of breaking the program if the user messes up
        # If the user enters valid input, the following indented block in 'try' will run
        try: 
            # Prompt the user to select a player by entering a number
            p_choice = int(input('Enter 1 for Gandalf, 2 for Gimli, 3 for Legolas or 4 for Aragorn: '))
            
            # Check if the input number is within the valid range
            if p_choice > 0 and p_choice <= 4:
                player = players[p_choice-1]  # Select the player based on the input number
                print(f'You have selected {player.name} the {player.race} {player.cls}!')
                weapon = weapons[p_choice-1]  # Select the corresponding weapon based on the input number
                print(f'You are equipped with {weapon.name}, the {weapon.wpn}!')
                player_selected = True  # Set the flag to True to exit the loop

        # If the code indented in the 'try' block does not work, the program will ignore it and run the 'except' block instead         
        except:
            # If the input is invalid, prompt the user to enter a valid number
            print('Fool of a Took! Enter a number in the correct range!')
