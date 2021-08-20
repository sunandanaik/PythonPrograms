import pygame
import random

pygame.init()
screen = pygame.display.set_mode((288,512))
pygame.display.set_caption("Flappy Bird Game")

background = pygame.image.load("Images/bg.PNG")
background=pygame.transform.scale(background, (288, 450)) #to resize background image
base = pygame.image.load('Images/base.jpg')


#Bird
bx = 100
by = 300
bjump = 0
bspeed = 0.5
birdimg = pygame.image.load('Images/bird.png')
birdimg=pygame.transform.scale(birdimg, (64, 64)) #to resize bird image

def draw_bird(bx,by):
    screen.blit(birdimg,(bx,by))

#Pipes
pipeupimg = pygame.image.load("Images/pillar-up.jpg")
pipedownimg = pygame.image.load("Images/pillar-down.jpg")

pipe1 = [300, -170] #[xcoord,ycoord]
pipe2 = [550, -100]
Pipes=[]
Pipes.append(pipe1)
Pipes.append(pipe2)

def draw_pipe(PIPE):
    screen.blit(pipeupimg,(PIPE[0],PIPE[1]))
    screen.blit(pipedownimg,(PIPE[0],PIPE[1]+420))

#Score
score = 0
font = pygame.font.Font('freesansbold.ttf',35)
sCoord = (10,10)
def print_score(scr):
    screen.blit(font.render("Score : "+str(scr), True,(255,255,255)),sCoord)

#Sounds in Game
dieSound=pygame.mixer.Sound('Sounds/die.mp3')
hitSound=pygame.mixer.Sound('Sounds/hit.mp3')
swooshSound=pygame.mixer.Sound('Sounds/Swoosh.mp3')
pointSound=pygame.mixer.Sound('Sounds/point.mp3')
wingSound=pygame.mixer.Sound('Sounds/wing.mp3')

#Game Loop infinite running
running = True 
while running:
    #screen.fill((120,120,255))
    screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type==pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                wingSound.play()
                bjump = 1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                bjump = 0

    #bird movement
    draw_bird(bx,by)

    #Bird jump functionality
    if bjump == 1:
        by -= 2
    else:
        by += bspeed

    #Pipe movement
    for p in Pipes:
        draw_pipe(p)
        p[0] -= 0.5
        if p[0] <= 0:
            p[0] = 500
            p[1] = random.randint(-250,-100)

    #GAME OVER functionality
    for p in Pipes:
        if p[0]  == 100: #when pipe reaches over the bird
            if by <= p[1]+320 or by >=p[1]+420:
                hitSound.play()
                dieSound.play()
                print("GAME OVER")
                running = False
            else:
                pointSound.play()
                score += 1
                print(score)

    print_score(score)
    screen.blit(base,(0,418))

    pygame.display.update()

