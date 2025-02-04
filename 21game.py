import random
import time


def lose():
    print ("\n\nYOU LOSE !")
    print("Better luck next time !")
    exit(0)


def check():
    xyz =[]
    i = 1
    while i < len(xyz):
        if(xyz[i] - xyz[i-1] != 1):
            return False
        i += 1
    return True


def nearestMultiple(num):
    if num >= 4:
        near = num + (4 - (num % 4))
    else:
        near = 4
    return near

def game_21():
    xyz = []
    # checks whether the numbers are consecutive
    last = 0
    while True:
        print ("Enter 'F' to take the first chance.")
        print("Enter 'S' to take the second chance.")
        chance = input('> ')
         
        # player takes the first chance
        if chance == "F":
            while True:
                if last == 20:
                    lose()
                else:
                    print ("\nYour Turn.")
                    print ("\nHow many numbers do you wish to enter?")
                    inp = int(input('> '))
                

                               

                     
                    if inp > 0 and inp <= 3:
                        comp = 4 - inp
                    else:
                        while inp >= 4:
                            print("\nPlease enter values(0 -3)!")
                            print ("\nHow many numbers do you wish to enter?")
                    i, j = 1, 1
 
                    print ("Now enter the values")
                    while i <= inp:
                        a = input('> ')
                        a = int(a)
                        xyz.append(a)
                        i = i + 1
                     
                    # store the last element of xyz.
                    last = xyz[-1] 
                     
                    # checks whether the input 
                    # numbers are consecutive
                    if check(xyz) == True: 
                        if last == 21:
                            lose()
                             
                        else:
                            #"Computer's turn."
                            while j <= comp:
                                xyz.append(last + j)
                                j = j + 1
                            print ("Order of inputs after computer's turn is: ")
                            print (xyz)
                            last = xyz[-1]
                    else:
                        print ("\nYou did not input consecutive integers.")
                        lose()
        elif chance == "S":
            comp = 1
            last = 0
            while last < 20:
                #"Computer's turn"
                j = 1
                while j <= comp:
                    xyz.append(last + j)
                    j = j + 1
                print ("Order of inputs after computer's turn is:")
                print (xyz)
                if xyz[-1] == 20:
                    lose()
                     
                else:
                    print ("\nYour turn.")
                    print ("\nHow many numbers do you wish to enter?")
                    inp = input('> ')
                    inp = int(inp)
                    i = 1
                    print ("Enter your values")
                    while i <= inp:
                        xyz.append(int(input('> ')))
                        i = i + 1
                    last = xyz[-1]
                    if check(xyz) == True:
                        # print (xyz)
                        near = nearestMultiple(last)
                        comp = near - last
                        if comp == 4:
                            comp = 3
                        else:
                            comp = comp
                    else:
                        # if inputs are not consecutive
                        # automatically disqualified
                        print ("\nYou did not input consecutive integers.")
                        # print ("You are disqualified from the game.")
                        lose()
            print ("\n\nCONGRATULATIONS !!!")
            print ("YOU WON !")
            exit(0)
             
        else:
            print ("wrong choice")
                         


    



















    