from asyncio.windows_utils import pipe
import random #for generating random numbers
import sys #we will use sys.exit to exit the program
import pygame
from pygame.locals import * #Basic pygame imports

#Global Variables for the game
FPS = 32 #Frames per second: no of frames in 1 sec
SCREENWIDTH = 289
SCREENHEIGHT = 511
SCREEN = pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT))
GROUNDY = SCREENHEIGHT * 0.8 #80% of screen used for ground pic
GAME_SPRITES = {}
GAME_SOUNDS = {}
PLAYER = 'Images/bird.png'
BACKGROUND= 'Images/bg.jpg'
PIPE = 'Images/pillar.jpg'

def welcomeScreen():
        #shows welcome image on screen
        playerx = int(SCREENWIDTH/5)
        playery = int((SCREENHEIGHT - GAME_SPRITES['player'].get_height())/2) #to place exact at center of screen
        messagex = int((SCREENWIDTH - GAME_SPRITES['message'].get_width())/2)
        messagey = int(SCREENHEIGHT * 0.8)
        basex = 0
        while True:
            for event in pygame.event.get():
                #if user clicks on cross button, then close the game
                if event.type == QUIT or (event.type==KEYDOWN and event.key==K_ESCAPE):
                    pygame.quit()
                    sys.exit()
                #if user presses space or up key,start the game
                elif event.type == KEYDOWN and (event.key==K_SPACE or event.key==K_UP):
                    return
                else:
                    #display on screen or blit screen
                    SCREEN.blit(GAME_SPRITES['background'],(0,0))
                    SCREEN.blit(GAME_SPRITES['player'],(playerx,playery))
                    SCREEN.blit(GAME_SPRITES['message'],(messagex,messagey))
                    SCREEN.blit(GAME_SPRITES['base'],(basex,GROUNDY))
                    pygame.display.update()
                    FPSCLOCK.tick(FPS) 

def getRandomPipe():
    #generate positions of two pipes (one bottom straight and another top rotated) for blitting on the screen
    pipeHeight = GAME_SPRITES['pipe'][0].get_height()
    offset = SCREENHEIGHT/3
    y2 = offset + random.randrange(0,int(SCREENHEIGHT - GAME_SPRITES['base'].get_height()-1.2 * offset))
    pipeX = SCREENWIDTH +10
    y1 = pipeHeight - y2 +offset
    pipe = [
           {'x':pipeX,'y':y1}, #upper pipe
           {'x':pipeX,'y':y2} #lower pipe
    ]
    return pipe

def isCollide(playerx,playery,upperPipes,lowerPipes):
    if playery > GROUNDY-25 or playery < 0:
        GAME_SOUNDS['hit'].play()
        return True
    for pipe in upperPipes:
        pipeHeight = GAME_SPRITES['pipe'][0].get_height()
        if playery < pipeHeight + pipe['y'] and (abs(playerx - pipe['x'] < GAME_SPRITES['pipe'][0].get_width())):
            GAME_SOUNDS['hit'].play()
            return True
    for pipe in lowerPipes:
        pipeHeight = GAME_SPRITES['pipe'][0].get_height()
        if playery > GAME_SPRITES['player'].get_height() + pipe['y'] and (abs(playerx - pipe['x'] < GAME_SPRITES['pipe'][0].get_width())):
            GAME_SOUNDS['hit'].play()
            return True

    return False

def mainGame():
        score=0
        playerx = int(SCREENWIDTH/5)
        playery = int(SCREENHEIGHT/5)
        basex=0
        #Create 2 pipes/pillars for blitting on the screen
        newPipe1 = getRandomPipe() #list returned
        newPipe2 = getRandomPipe() #list returned
        #my list of upper pipes
        upperPipes = [
            {'x':SCREENWIDTH+200,'y':newPipe1[0]['y']},
            {'x':SCREENWIDTH+200+SCREENWIDTH/2,'y':newPipe2[0]['y']}
        ]
        #my list of lower pipes
        lowerPipes = [
            {'x':SCREENWIDTH+200,'y':newPipe1[1]['y']},
            {'x':SCREENWIDTH+200+SCREENWIDTH/2,'y':newPipe2[1]['y']}
        ]
        pipeVelocityX = -4
        playerVelocityY = -9
        playerMaxVelY = 10
        playerMinVelY = -8
        playerAccY = 1

        playerFlapVelocity = 8 #bird velocity while flapping
        playerFlapped = False # it is true only when the bird is flapping

        while True:
            for event in pygame.event.get():
                if event.type == QUIT or (event.type==KEYDOWN and event.key==K_ESCAPE):
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN and (event.key==K_SPACE or event.key==K_UP):
                    if playery > 0: #if player is in screen
                        playerVelocityY = playerFlapVelocity
                        playerFlapped = True
                        GAME_SOUNDS['wing'].play()
            #outside for loop
            crashTest = isCollide(playerx,playery,upperPipes,lowerPipes)#this function will return true if the player is crashed
            if crashTest:
                return
            #check for score
            playerMidPos = playerx + GAME_SPRITES['player'].get_width()/2
            for pipe in upperPipes:
                pipeMidPos = pipe['x'] + GAME_SPRITES['pipe'][0].get_width()/2
                if pipeMidPos <= playerMidPos:
                    score+=1
                    print(f"Your Score is : {score}")
                GAME_SOUNDS['point'].play()
            
            if playerVelocityY < playerMaxVelY and not playerFlapped:
                playerVelocityY += playerAccY
            if playerFlapped:
                playerFlapped = False
            playerHeight = GAME_SPRITES['player'].get_height()
            playery = playery + min(playerVelocityY, GROUNDY-playery-playerHeight)

            #move pipes to the left
            for upperPipe, lowerPipe in zip(upperPipes,lowerPipes):
                upperPipe['x'] +=pipeVelocityX
                lowerPipe['x'] +=pipeVelocityX
            #Add a new pipe when the first is about to cross the leftmost part of the screen
            if 0 < upperPipes[0]['x'] < 5:
                newpipe= getRandomPipe()
                upperPipes.append(newpipe[0])
                lowerPipes.append(newpipe[1])

            #if the pipe is out of screen, remove it
            if upperPipes[0]['x'] < -GAME_SPRITES['pipe'][0].get_width():
                upperPipes.pop(0)
                lowerPipes.pop(0)
            #lets blit our sprites now
            SCREEN.blit(GAME_SPRITES['background'],(0,0))
            #move pipes to the left
            for upperPipe, lowerPipe in zip(upperPipes,lowerPipes):
                SCREEN.blit(GAME_SPRITES['pipe'][0],(upperPipe['x'],upperPipe['y']))
                SCREEN.blit(GAME_SPRITES['pipe'][1],(lowerPipe['x'],lowerPipe['y']))
            SCREEN.blit(GAME_SPRITES['base'],(basex, GROUNDY))
            SCREEN.blit(GAME_SPRITES['player'],(playerx, playery))
            myDigits = [int(x) for x in list(str(score))]
            width = 0
            for digit in myDigits:
                width += GAME_SPRITES['numbers'][digit].get_width()
            Xoffset = (SCREENWIDTH - width)/2

            for digit in myDigits:
                SCREEN.blit(GAME_SPRITES['numbers'][digit],(Xoffset,SCREENHEIGHT * 0.12))
                Xoffset =+ GAME_SPRITES['numbers'][digit].get_width()
            pygame.display.update()
            FPSCLOCK.tick(FPS)




if __name__=="__main__":
    #this will be the main function from where game will start
    pygame.init() #initializes all modules of pygame
    FPSCLOCK = pygame.time.Clock() #controlles FPS of game
    pygame.display.set_caption('Flappy Bird Game by Sunanda')
    GAME_SPRITES['numbers']=(
        pygame.image.load('Images/0.png').convert_alpha(),
        pygame.image.load('Images/1.png').convert_alpha(),
        pygame.image.load('Images/2.png').convert_alpha(),
        pygame.image.load('Images/3.png').convert_alpha(),
        pygame.image.load('Images/4.png').convert_alpha(),
        pygame.image.load('Images/5.png').convert_alpha(),
        pygame.image.load('Images/6.png').convert_alpha(),
        pygame.image.load('Images/7.png').convert_alpha(),
        pygame.image.load('Images/8.png').convert_alpha(),
        pygame.image.load('Images/9.png').convert_alpha()
        )
    GAME_SPRITES['message']=pygame.image.load('Images/welcomemsg.png').convert_alpha()
    GAME_SPRITES['base']=pygame.image.load('Images/base.jpg').convert_alpha()
    GAME_SPRITES['pipe']=(
        pygame.transform.rotate(pygame.image.load(PIPE).convert_alpha(),180),
        pygame.image.load(PIPE).convert_alpha()
    )

    #Game Sounds
    GAME_SOUNDS['die'] = pygame.mixer.Sound('Sounds/die.mp3')
    GAME_SOUNDS['hit'] = pygame.mixer.Sound('Sounds/hit.mp3')
    GAME_SOUNDS['point'] = pygame.mixer.Sound('Sounds/point.mp3')
    GAME_SOUNDS['swoosh'] = pygame.mixer.Sound('Sounds/Swoosh.mp3')
    GAME_SOUNDS['wing'] = pygame.mixer.Sound('Sounds/wing.mp3')

    GAME_SPRITES['background'] = pygame.image.load(BACKGROUND).convert() #only changes images
    GAME_SPRITES['player'] = pygame.image.load(PLAYER).convert_alpha() #changes pixels of images
    #to resize player & background images
    GAME_SPRITES['background'] = pygame.transform.scale(GAME_SPRITES['background'], (SCREENWIDTH, SCREENHEIGHT))
    GAME_SPRITES['player'] = pygame.transform.scale(GAME_SPRITES['player'], (100, 100))
    
    #print(GAME_SPRITES['player'].get_rect().size) # you can get size

    while True:
        welcomeScreen() #shows welcome screen to user until he presses the button
        mainGame()  #this is the main game function






