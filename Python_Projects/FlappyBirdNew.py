import pygame
import random

pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Flappy Bird Game")

#Bird
bx = 200
by = 300
bjump = 0
bspeed = 0.3
def draw_circle(bx,by):
    pygame.draw.circle(screen, (255,0,0),(bx,by),30) #circle(surface,color,position,radius)

#Pipes
#pipe1 = [600,0,50,150] #left,top,width,height
pipe1 = [800,0,50,random.randint(50,250)]
pipe2 = [400,0,50,random.randint(50,250)]
Pipes=[]
Pipes.append(pipe1)
Pipes.append(pipe2)

def draw_pipe(PIPE):
    #left,top,width,height
    #Top Pipe
    pygame.draw.rect(screen,(0,255,0),(PIPE[0],PIPE[1],PIPE[2],PIPE[3]))#rect(surface,color,pipe1 parameters)
    #Bottom Pipe
    pygame.draw.rect(screen,(0,255,0),(PIPE[0],300+PIPE[3],PIPE[2],PIPE[3]+200))#rect(surface,color,pipe2 parameters)

#Score
score = 0
font = pygame.font.Font('freesansbold.ttf',35)
sCoord = (10,10)
def print_score(scr):
    screen.blit(font.render("Score : "+str(scr), True,(255,255,255)),sCoord)

#Game Loop infinite running
running=True
while running:
    screen.fill((120,120,255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #Bird jumping code    
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bjump = 1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                bjump = 0
    
    #Bird Movement
    draw_circle(bx,by) #function calling

    #Bird jump functionality
    if bjump == 1:
        by -= 2
    else:
        by += bspeed

    #Pipe Movement
    for p in Pipes:
        draw_pipe(p)
        p[0] -= 0.5
        if p[0] <= 0:
            p[0] = 800
            p[3] = random.randint(50,250)
    
    #GAME OVER functionality
    for p in Pipes:
        if p[0]  == 200: #when pipe reaches over the bird
            if by <= p[3] or by >= 300+p[3]:
                print("GAME OVER")
                running = False
            else:
                score += 1
                print(score)

    print_score(score)
    pygame.display.update()
