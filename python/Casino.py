# import libraries or packages
from random import randint 
import os 

# functions
def rollDices():
    dice1 = randint(1,6)
    dice2 = randint(1,6)
    return dice1, dice2 
    return dice1, dice2 
   
# declare and initialize variables and/or constants
Player_lives = 3
dice1 = 0
dice2 = 0
roll_count = 0
equal_count = 0
acum_dices = 0
status=True


# Main 
print(" welcom to casino :::")
press_key = input("\nPress any key to start the game :::")
while status:
    os.system('cls')
    dices = rollDices()
    roll_count += 1
    dices_add = 0
    print("#"* 20)
    print(f"Roll dices N°.: {roll_count}")
    print("#"* 20)
    print(f"Player lives: {Player_lives}")

    if acum_dices > 14:
        dicex = dices[randint(0, 1)]
        print(f"dice: {dicex}")
        acum_dices += dicex
    else:     
        print(f"dice 1: {dices[0]}")
        print(f"dice 2: {dices[1]}")
        dices_add = dices[0] + dices[1]
        acum_dices += dices_add

    if acum_dices >=20:
        print("::: congratulations, you ve win:::")
        break

    if dices_add % 2 != 0:
        Player_lives-=1
        print(f"you ' ve lost one live ::: Now you have {Player_lives} lives")
        if Player_lives == 0:
            print("::: GAME OVER :::")
            break

if  dices[0] == 6 and dices[1] == 6 or dices[0]==1 and dices[1] == 1:
    Player_lives+=1
    print("you 've win one live :::")
    print(f"Dices addition: {dices_add}")

    if Player_lives == 0:
       print(":::game over:::")
       print(f"roll count: {roll_count}")

print(f"dices adddition: {dices_add}")
print(f"dices acum: {acum_dices}")
if roll_count==5:
    break
else: 
press_key = input("\nPress any key to roll dices again")