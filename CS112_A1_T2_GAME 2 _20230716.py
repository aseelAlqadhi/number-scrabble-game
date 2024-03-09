
# FILE : CS112_A1_T2_2_20230716.py

#GAME DESCRIPTION : Number scrabble is a game played by two players each player has to choose 3 numbers from 1 to 9 that add up to 15 , the player that reaches 15 first wins

# AUOTHER : Aseel Mohammed Hatem Alqadhi

# ID :  20230716


print ("************************************************************************************")
print ("choose three numbers from 1 to 9 that add up to 15 ,the first player reaches 15 wins ")
print ("************************************************************************************")


def winner(chosen_n):        # function to check the winner
    for x in range(len(chosen_n)):
        for y in range(x+1,(len(chosen_n))):
            for z in range (y+1,(len(chosen_n))):
                if chosen_n[x] +chosen_n[y]+chosen_n[z] ==15 :
                    return True

    return False

def sum_of_nums():
    numbers = [1,2,3,4,5,6,7,8,9]
    player1_list = []
    player2_list = []

    for turn in numbers:   #for loop that iterates through each turn
            print("first player's turn")
            print(" Available numbers :", numbers)
            chosen_n = int(input("choose a number: "))
            print("-----------------------------------")
            if chosen_n not in numbers:
                print("invalid number, try again ")
                continue
                print("first player's turn")
                print(" Available numbers :", numbers)
                chosen_n = int(input("choose a number: "))
                print("-----------------------------------")
            player1_list.append(chosen_n)        #add the chosen number to player/s list
            numbers.remove(chosen_n)             #remove the chosen number from the list
            print("second's player turn")
            print(" numbers remained :", numbers)
            chosen_n = int(input("choose a number: "))
            print("-----------------------------------")
            if winner(player1_list):
                print("** Player 1 wins **")
                return
            if chosen_n not in numbers:
                print("invalid number, try again ")
                continue
                print("second player's turn")
                print(" Available numbers :", numbers)
                chosen_n = int(input("choose a number: "))
                print("-----------------------------------")
            player2_list.append(chosen_n)         #add the chosen number to player/s list
            numbers.remove(chosen_n)               #remove the chosen number from the list
            if winner(player2_list):
                print("** Player 2 wins **")
                return

    print("the game is a draw!")

sum_of_nums()
