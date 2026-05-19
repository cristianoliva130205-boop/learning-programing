from random import randint

# functions
def roll_dices():
    dice1 = randint(1, 6)
    dice2 = randint(1, 6)
    return dice1, dice2


dices = roll_dices()
print(dices)
print(f"dice 1: {dices[0]}")
print(f"dice 2: {dices[1]}")

if (dices[0] == dices[1]):
    print("you ve win ")
else:
    print("try again !!!")


status = 
count = 10

while status:
      dice1 = randint(1, 6)
      dice2 = randint(1, 6)

print(f"dice1: {dice1}")
print(f"dice2: {dice2}")

if dice1 == dice2:
     print("your win!")
     status=False

else:
     print("")

