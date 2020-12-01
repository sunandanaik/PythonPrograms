import random

def checkBoard(board):
    for player in range(1,3):
        if player==1:
            symbol="X"
        else:
            symbol="O"
        for i in range(0,3):
            if(board[i][0]==symbol) and(board[i][1]==symbol) and (board[i][2]==symbol):  #row
                return player+1
        print("Player ",player," did not capture any row.")
        for i in range(0,3):
            if(board[0][i]==symbol) and(board[1][i]==symbol) and (board[2][i]==symbol): #col
                return player+1
        
        if(board[0][0]==symbol) and(board[1][1]==symbol) and (board[2][2]==symbol): #diagonal-1
                return player+1
        
        if(board[0][2]==symbol) and(board[1][1]==symbol) and (board[2][0]==symbol):  #diagonal-2
                return player+1
    for i in range(0,3):
        for j in range(0,3):
            if board[i][j]=="":
                return 0
    return 1
            
def printBoard(board):
    #Write code to print the current board of the game
    cellstr=""
    print("-------------------")
    for i in range(0,3):
        for j in range(0,3):
            if board[i][j]=="":
                cellstr=" "
            elif board[i][j]=="X":
                cellstr="X"
            else:
                cellstr="O"
            print("|",cellstr,end="")
        print("|")
        if i<2:
            print("______________________")
    print()
    
def playMove(board,players,player):
    print(players[player]," will take move now")
    row=int(input("Choose Row where you want to put your bet :"))
    column=int(input("Choose Column where you want to put your bet :"))
    if player==1:
        board[row-1][column-1]="X"
    else:
        board[row-1][column-1]="O"
    
    printBoard(board)
    
def whoWillStart():
    #returns who will start the game
    return random.randint(1,2)

def startGame(board,players,player):
    initializeBoard(board)
    players[1]=input("Enter name of the Player 1(Symbol X) :")
    players[2]=input("Enter name of the Player 2(Symbol O) :")
    print(players[player]," won the toss. So ",players[player]," will start first")
    print()
    
def initializeBoard(board):
    for i in range(0,3):
        for j in range(0,3):
            board[i][j]=""
            
def togglePlayer(playerInGame):
    if playerInGame==1:
        return 2
    else:
        return 1
    
def announceResult(state,status,players):
    if status[state]=="DRAW":
        print("Game results in a draw")
    elif status[state]=="P1-WIN":
        print(players[1]," won the game.Congratulations!!")
    elif status[state]=="P2-WIN":
        print(players[2]," won the game.Congratulations!!")
    print()
    return int(input("Do you want to play again (Enter 1 for yes, 0 for No ):"))

def restartGame(board,players,whoStarted):
    initializeBoard(board)
    whoStarted=togglePlayer(whoStarted)
    print("In this game ",players[whoStarted]," will start the game")
    return whoStarted

#Main Program

#Variables required
board=[["O","X","O"],["X","X","O"],["O","","X"]]

players=["","P1","P2"]

status=["PLAY","DRAW","P1-WIN","P2-WIN"]

playerInGame=0  #1-"X" and 2-"O"
state=0
whoStarted=0
playerInGame=whoWillStart()
whoStarted=playerInGame
startGame(board,players,playerInGame)
#print(board)
playMove(board,players,playerInGame)

#Game Loop
while True:
    playMove(board,players,playerInGame)
    state=checkBoard(board)
    print(state)
    if status[state]=="PLAY":
        playerInGame=togglePlayer(playerInGame)
    else:
        playmore=announceResult(state,status,players)
        if playmore==1:
            playerInGame=restartGame(board,players,whoStarted)
            whoStarted=playerInGame
        else:
            print("Thanks for Playing!!")
            break
