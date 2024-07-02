
# this file is the main file for the program
#--------------------------------------------

# Import modules and classes
from game_objects import Weapon, Enemy
import random # import the random module
import time # import the time module

# Create weapons
w1 = Weapon('Face Smasher', 'Mace', 15)
w2 = Weapon('Sword of Slaying', 'Sword', 10)
weapons = [w1, w2]

# Create enemies
e1 = Enemy('Azog', 'Orc Warrior', 10, 100)
e2 = Enemy('Saruman', 'Human Wizard', 20, 40)
enemies = [e1, e2]

#Global Variables
game_over = False
player_health = 100
player_attack = 1

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
    while enemyX == exitX and enemyX == exitY:
        enemyX = random.randint(0, 4)
        enemyY = random.randint(0, 4)

gameBoard[enemyX][enemyY] = 2

weapon = weapons[random.randint(0, 1)]
print(f'You equip: {weapon.name}')

# ----------------------------------------- SET UP THE FUNCTIONS -----------------------------------------
# create the def() functions for the program here
def printBoard():
    for row in gameBoard:
        print(row)

def Fight():
    global enemy, player_health, player_attack, game_over, enemies_defeated
    
    print(f'You encounter {enemy.name} the {enemy.type}!')
    choice = ''
    while choice.lower() != 'r' and player_health >= 0 and enemy.health >= 0:
        choice = input('A to attack, R to run: ')
        if choice.lower() == 'a':
            player_health -= enemy.dmg
            enemy.health -= (player_attack + weapon.dmg)
            print(f'{enemy.name} deals {enemy.dmg} damage to you! Your health is now {player_health}!')
            print(f'You have dealt {player_attack + weapon.dmg} with your {weapon.name}! The enemy is now on {enemy.health} health!')
        elif choice.lower() == 'r':
            break
        else:
            print('Choose again plz')

    if enemy.health <= 0:
        print('Congratulations, you beat the enemy!')
        enemies_defeated = True
    elif player_health <= 0:
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
while game_over == False:
    printBoard()
    movePlayer()
    checkExit()
    time.sleep(1)
print('Game over!')