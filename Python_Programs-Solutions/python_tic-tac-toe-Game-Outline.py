#Variables required
board=[["","",""],["","",""],["","",""]]

players=["","P1","P2"]

status=["PLAY","OVER","P1-WIN","P2-WIN"]

playerInGame=1  #1-"X" and 2-"O"

state=0

whoStarted=0


#Code to initialize board to start new game
def initializeBoard(board):
    pass

#Code to start game for the first time. Initialize board and ask for player Names
def startGame(board,players):
    pass

#Write code to print the current board of the game
def printBoard(board):
    pass

#write code for player to play her move
def playMove(board,players,player):
    pass

#check and returns the status whether it is draw,game on, P1 wins or P2 wins
def checkWinningCondition(board):
    pass

#Code to restart game if players want to play more
def restartGame(board,players,whoStarted):
    pass

#returns who will start the game
#random.randint(1,2)
def whoWillStart():
    pass

#change the current player who will take the next move
def togglePlayer(player,players):
    pass

#write code to announce the winner for draw and take option for playing again
def announceResult(state,status,players):
    pass

#Main Program
startGame(board,players)

playerInGame=whoWillStart()

whoStarted=playerInGame

#Game Loop
while True:
    playMove(board,players,playerInGame)
    state=checkWinningCondition(board)
    if status[state]=="PLAY":
        togglePlayer(playerInGame,players)
    else:
        playMore=announceResult(state,status,players)
        if playMore=="YES":
            playerInGame=restartGame(board,players,whoStarted)
        else:
            print("Thanks for Playing!!")
            break