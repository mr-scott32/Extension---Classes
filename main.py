
# this file is the main file for the program
#--------------------------------------------

# Import modules and classes
from game_objects import Weapon, Enemy, Player # Import the Weapon, Enemy and Player classes from game_objects.py for use
import random # import the random module
import time # import the time module


# Create characters
players = [Player('Gandalf', 'Human', 'Wizard', 2, 100),
           Player('Gimli', 'Dwarf', 'Fighter', 3, 180),
           Player('Legolas', 'Elf', 'Archer', 1, 120 ),
           Player('Aragorn', 'Human', 'Ranger', 4, 130)]

# Create weapons
weapons =  [Weapon('Glamdring', 'Sword', random.randint(8, 12)), 
            Weapon("Balin's Axe", 'Greataxe', random.randint(12, 15)), 
            Weapon('Bow of the Galadhrim', 'Longbow', random.randint(10, 12)),
            Weapon('Anduril', 'Great Sword', random.randint(10, 14))]

# Create enemies
enemies = [Enemy('Azog', 'Orc Warrior', random.randint(15, 18), random.randint(80, 140)),
           Enemy('Saruman', 'Human Wizard', random.randint(20, 30), random.randint(60, 100))]


#Global Variables
game_over = False
player = ''
weapon = ''

enemies_defeated = False


#----------------------------------------- SET UP THE GAME BOARD -----------------------------------------
#create a 5x5 game board. 0 = empty, 1 = player, 2 = enemy, 3 = treasure, 4 = trap, 5 = exit, 6 = boss, 7=visited
gameBoard = [[0,0,0,0,0],
             [0,0,0,0,0],
             [0,0,0,0,0],
             [0,0,0,0,0],
             [0,0,0,0,0]]

# place the player in the middle of the game board
playerX = 2
playerY = 2
gameBoard[playerX][playerY] = 1



# place the exit in a random location
exitX = random.randint(0,4)
exitY = random.randint(0,4)
while exitX == playerX and exitY == playerY:
    exitX = random.randint(0,4)
    exitY = random.randint(0,4) 
gameBoard[exitX][exitY] = 5

enemy = enemies[random.randint(0, 1)]

enemyX = random.randint(0, 4)
enemyY = random.randint(0, 4)

while enemyX == playerX and enemyX == playerY:
    enemyX = random.randint(0, 4)
    enemyY = random.randint(0, 4)
    while enemyX == exitX and enemyX == exitY:
        enemyX = random.randint(0, 4)
        enemyY = random.randint(0, 4)

gameBoard[enemyX][enemyY] = 2






# ----------------------------------------- SET UP THE FUNCTIONS -----------------------------------------
# create the def() functions for the program here
def selectPlayer():
    global player, weapon
    player_selected = False
    while player_selected == False:
        try: 
            p_choice = int(input('Enter 1 for Gandalf, 2 for Gimli, 3 for Legolas or 4 for Aragorn: '))
            if p_choice > 0 and p_choice <= 4:
                player = players[p_choice-1]
                print(f'You have selected {player.name} the {player.race} {player.cls}!')
                weapon = weapons[p_choice-1]
                print(f'You are equipped with {weapon.name}, the {weapon.wpn}!')
                player_selected = True
        except:
            print('Fool of a Took! Enter a number in the correct range!')



def printBoard():
    for row in gameBoard:
        print(row)

def Fight():
    global enemy, player, game_over, enemies_defeated, weapon
    
    print(f'You encounter {enemy.name} the {enemy.type}!')
    choice = ''
    while choice.lower() != 'r' and player.health > 0 and enemy.health > 0:
        choice = input('A to attack, R to run: ')
        if choice.lower() == 'a':
            player.health -= enemy.dmg
            enemy.health -= (player.atk + weapon.dmg)
            print(f'{enemy.name} deals {enemy.dmg} damage to you! Your health is now {player.health}!')
            print(f'You have dealt {player.atk + weapon.dmg} with {weapon.name}! The enemy is now on {enemy.health} health!')
        elif choice.lower() == 'r':
            break
        else:
            print('Choose again plz')

    if enemy.health <= 0:
        print(f'Congratulations, you beat {enemy.name}!')
        enemies_defeated = True
    if player.health <= 0:
        print('Death comes for us all...')
        game_over = True

        
        
        


def movePlayer():
    global playerX, playerY, enemyX, enemyY
    direction = input('Enter the direction you want to move (N,S,E,W): ')
    direction = direction.lower()
    if direction == 'n':
        if playerX > 0:
            gameBoard[playerX][playerY] = 7
            playerX -= 1
            gameBoard[playerX][playerY] = 1
        else:
            print('You cannot move in that direction')
    elif direction == 's':
        if playerX < 4:
            gameBoard[playerX][playerY] = 7
            playerX += 1
            gameBoard[playerX][playerY] = 1
        else:
            print('You cannot move in that direction')
    elif direction == 'e':
        if playerY < 4:
            gameBoard[playerX][playerY] = 7
            playerY += 1
            gameBoard[playerX][playerY] = 1
        else:
            print('You cannot move in that direction')
    elif direction == 'w':
        if playerY > 0:
            gameBoard[playerX][playerY] = 7
            playerY -= 1
            gameBoard[playerX][playerY] = 1
        else:
            print('You cannot move in that direction')
    else:
        print('I do not understand that direction')
    
    if enemyX == playerX and enemyY == playerY:
        Fight()
    

#check if the player has reached the exit
def checkExit():
    global game_over
    if playerX == exitX and playerY == exitY:
        print('You have reached the exit')
        if enemies_defeated == True:
            game_over = True
            print('You win!')
        else:
            print('Go defeat the enemies first!')

# ----------------------------------------- MAIN LOOP -----------------------------------------
# create the main loop for the program here
selectPlayer()
while game_over == False:
    printBoard()
    movePlayer()
    checkExit()
    time.sleep(1)
print('Game over!')