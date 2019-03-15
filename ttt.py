from tttlib import *
print("Welcome to the game of Tic-Tac-Toe")
BoardCondition = genBoard()
printBoard(BoardCondition)
while True:
        while True:
                moveX = input("Player 1:Enter the position that you would like to select: ")
                if (int(moveX) >= 0) and (int(moveX)<=8) and (BoardCondition[int(moveX)] == 0):
                        BoardCondition[int(moveX)] = 1
                        break
                else:
                        print ("Invalid input")
        state = analyzeBoard(BoardCondition)
        if not (state == -1):
                printBoard(BoardCondition)
                print ("")
        if state == 1:
                print ("Congratulations!Player 1 has won the game!")
                break
        elif state == 3:
                print ("It's a tie.")
                break
        moveO = genWinningMove(BoardCondition,2)
        if moveO == -1:
                print ("True")
                moveO = genNonLoser(BoardCondition,2)
                if moveO == -1:
                        print ("Fact")
                        moveO = genRandomMove(BoardCondition,2)
        BoardCondition[moveO] = 2
        state = analyzeBoard(BoardCondition)
        if not (state == -1):
                printBoard(BoardCondition)
                print ("")
        if state == 2:
                print ("The computer has won the game")
                break
        elif state == 3:
                print ("It's a tie")
                break
~                                           
