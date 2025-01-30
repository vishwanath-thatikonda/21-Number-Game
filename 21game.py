import random
import time

def lost():
    pass



def game_21():
     pass

print("Player 2 is Computer.")
player = input("Do you want to start the game? (Yes/No) : ").lower()


while player.isdigit():
    print("Invalid input. Please Enter YES to start and NO to stop!")
    player = input("Do you want to start the game? (Yes/No) : ").lower()

while player == 'yes':
    print("Enter 'F' to take the first chance.")
    print("Enter 'S' to take the second chance.")
    chance = input('> ').upper()
    if chance.isdigit():
        print("Enter a valid input!,'F' to take the first chance or 'S' to take the second chance. ")
        chance = input('> ').upper()

    if chance == 'F':
        break
    elif chance == 'S':
        break

    break

if player == 'no':
    print("Thank you! you ended the game!")











    