import random
def genBoard():
        Condition = [0,0,0,0,0,0,0,0,0]
        return Condition

#function that takes in a list "T" which contains the information about the board's condition, and check if there is any error. If there is,
#then return False. Otherwise,print the gameboard and return True.
def printBoard(T):
        #declare a list that contains the numbering of the gameboard(0 to 8,which corresponds to every element in T )
        BoardPosition = [0,1,2,3,4,5,6,7,8]
        #check if the length of the list "T" is 9.If it is not,return False
        if len(T) != 9:
                return False
        #check if the variable "T" that is being passed to the function belongs to the type list. If it is not, return False.
        elif not (type(T) == list):
                return False
        #check every element in the list for their validity
        for i in range(0,len(T)):
                #if the element is 0,which means that the position is unoccupied,nothing happens
                if T[i] == 0:
                        BoardPosition[i] = BoardPosition[i]
                #if the element is 1,which means that player1 has chosen this particular position,change the corresponding element in the                    #board numbering list to be "X" for display                
                elif T[i] == 1 :
                        BoardPosition[i] = "X"
                #if the element is 2,which means that player2 has chosen this position,change the corresponding element in the board 
                #numbering list to be "O" for display
                elif T[i] == 2:
                        BoardPosition[i] = "O"
                #if none of the above situation occurs,which implies that there is an error,return false
                else:
                        return  False
        #print the gameboard
print (" " + str(BoardPosition[0]) + " | " + str(BoardPosition[1]) + " | " + str(BoardPosition[2]))
        print ("---|---|---")
        print (" " + str(BoardPosition[3]) + " | " + str(BoardPosition[4]) + " | " + str(BoardPosition[5]))
        print ("---|---|---")
        print (" " + str(BoardPosition[6]) + " | " + str(BoardPosition[7]) + " | " + str(BoardPosition[8]))
        #return True at the end of the function as it is able to run without error and successfully prints out the gameboard
        return True
#function that determines the state of the game 
def analyzeBoard(t):
        if (len(t) != 9):
                return -1
        for i in range(0,len(t),1):
                if type(t[i]) != int:
                        return -1
        if t[0] == t[1] == t[2] != 0:
                return t[0]
        if t[3] == t[4] == t[5] != 0:
                return t[3]
        if t[6] == t[7] == t[8] != 0:
                return t[6]
        if t[0] == t[3] == t[6] != 0:
                return t[0]
        if t[1] == t[4] == t[7] != 0:
                return t[1]
        if t[2] == t[5] == t[8] != 0:
                return t[2]
        if t[0] == t[4] == t[8] != 0:
                return t[0]
        if t[2] == t[4] == t[6] != 0:
                return t[2]
        n_opens=0
        for i in t:
                if i==0:
                        n_opens+=1
        if n_opens == 0:
                return 3
        else:
                return 0
#function that generates a position on the board that prevents the opponent from winning 
def genNonLoser(T,player):
        if analyzeBoard(T) != 0:
                return -1
        if player == 1:
                opp = 2
        elif player == 2:
                opp = 1
        else:
                return -1
        for i in range(0,9,1):
                NewPosition = list(T)
                if NewPosition[i] == 0:
                        NewPosition[i] = opp
                        if analyzeBoard(NewPosition) == opp:
                                return i
        return -1
#function that generates a position on the board that allows the player to win,if possible  
def genWinningMove(T,player):
        if analyzeBoard(T) != 0:
                return -1
        for i in range(0,9,1):
                NewPosition = list(T)
                if NewPosition[i] == 0:
                        NewPosition[i] = player
                        if analyzeBoard(NewPosition) == player:
                                return i
        return -1
#function that generates a random position on the board that is open
def genRandomMove(T,player):
        if analyzeBoard(T) != 0:
                return -1
        if (player != 1) and (player != 2):
                return -1
        canExit = False
        while canExit == False:
                rand = random.randint(0,8)
                canExit = True
                if (T[rand] != 0 ):
                        canExit = False
        return rand
        #function that generates an open move for the player (in this case,the first position on the board that is open)
def genOpenMove(T,player):
        if analyzeBoard(T) != 0:
                return -1
        if (player != 1) and (player != 2):
                return -1
        for i in range(0,9,1):
                if T[i] == 0:
                        return i
        return -1

                                                    
