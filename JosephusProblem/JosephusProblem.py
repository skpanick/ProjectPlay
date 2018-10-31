
__author__ =  "ShreejithPanicker(esc777)"
__description__ = "A simple program to show the Josephus Problem where every 2nd person is killed."

import math
def formula_out(circle):
    '''
	Shows the working of the formula
    '''
    print("winner is " + str(int(2*(circle - math.pow(2,math.floor(math.log2(circle)))) + 1)))
    print("closest power of 2 is "+str(int(math.pow(2,math.floor(math.log2(circle)))))+" i.e. 2^"+str(int(math.floor(math.log2(circle)))))        
def play_game(circle):
    '''
	Kills the next person until only one remains
    '''
    kill_list = list(range(1,circle+1))
    i = 1
    while (len(kill_list)> 1):
        print("Kill : "+str(kill_list[i]))
        old_i = i
        if i < len(kill_list) - 2:
            i = i + 1
        else:
            if kill_list[i] == kill_list[-1]:
                i = 1
            else:
                i = 0
        del kill_list[old_i]
    print("survives : "+str(kill_list[0]))
def the_game():
    '''
    Control function
    '''
	#Size of the circle
    circle = int(input("What is the size of your circle? : "))
    formula_out(circle)
    playGame = input("Want to see it play kill by kill (Y/N)? : ")
    if (playGame.lower() == "Y".lower()):
        play_game(circle)
#Main code
choice = "Y"
while(choice.lower() == "Y".lower()):
    the_game()
    choice = input("\nwanna continue (Y/N)? : ")