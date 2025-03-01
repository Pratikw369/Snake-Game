#snake game
import pygame
import random
import time
import os
import sys
pygame.init()
pygame.mixer.init()
collect = pygame.mixer.Sound("beep-07a.mp3")
collect.play()
gameov = pygame.mixer.Sound("beep-02.mp3")
#gamewindow


#snake food and snake


#game specific


#colors
white =(255,255,255)
red =(255,0,0)
green =(0,255,0)
blue = (0,0,255)
black = (0,0,0)
screen_width = 900
screen_height = 600
gamewindow = pygame.display.set_mode((screen_width,screen_height))



#Printing scoreboard
font = pygame.font.SysFont(None,40)
def text_screen(text,color,x,y):
    screen_text = font.render(text,True,color)
    gamewindow.blit(screen_text,[x,y])
    
#snake length
def plot_snake(gamewindow,color,snk_list,snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gamewindow,blue,[ x, y,snake_size,snake_size])
        
def welcome():
    exit_game =False
    while not exit_game:
        gamewindow.fill((255,255,255))
        text_screen("Welcome to Little Snake",black,260,270)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                exit_game = True
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    gameloop() 
                if event.key == pygame.K_ESCAPE:
                    exit_game = True
    pygame.quit()
    sys.exit()                    

pygame.display.set_caption('Little Snake')
pygame.display.update
clock =pygame.time.Clock()

def gameloop():
    exit_game = False
    game_over = False
    score = 0
    if not os.path.exists("highscore.txt"):
        with open("highscore.txt","w") as f:
            f.write("0")
    with open('highscore.txt',"r") as f:
        highscore = f.read()
    snake_x=55
    snake_y=55
    snake_size=50
    food_size = 50
    food_x = random.randrange(50,int(screen_width-100))
    food_y = random.randrange(50,int(screen_height-100))
    vel = 6
    fps = 70
    velocity_x = 0
    velocity_y = 0  
    snk_list =[]
    snk_length =0

    while not exit_game:
        
        
            
            

        if game_over:    
            with open('highscore.txt',"w") as f:
                f.write(str(highscore))
            gamewindow.fill(white)
            text_screen('GAME OVER! press Enter to continue' ,red,190,270)
            text_screen('Score: '+str(score) ,green,374,307)
            for event in pygame.event.get():
                #print(event)
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN :
                        gameloop()
                    if event.key == pygame.K_ESCAPE:
                        welcome()
             
        else:    
        
            for event in pygame.event.get():
                #print(event)
                if event.type == pygame.QUIT:
                    exit_game = True
                
                if event.type == pygame.KEYDOWN:
                
                    if event.key == pygame.K_RIGHT:
                        velocity_x = vel
                        velocity_y = 0
                    if event.key == pygame.K_LEFT:
                        velocity_x = -vel
                        velocity_y = 0
                    if event.key == pygame.K_UP:
                        velocity_y = -vel
                        velocity_x = 0
                    if event.key == pygame.K_DOWN:
                        velocity_y = vel
                        velocity_x = 0
                    if event.key == pygame.K_0:
                        highscore = 0
                    if event.key == pygame.K_ESCAPE:
                        welcome()
                
                            
            snake_x += velocity_x
            snake_y += velocity_y
            if abs(snake_x - food_x) <49 and abs(snake_y -food_y) <49:
            
                collect.play()
                food_x = random.randrange(50,int(screen_width-100))
                food_y = random.randrange(50,int(screen_height-100))
                score+=1
                
                # print(highscore)
                if score > int(highscore):
                    highscore = score
                
                #print(('\a'),score)
                snk_length+= 5
                
                
        
                
                                
            gamewindow.fill(white)
            text_screen('Score: '+str(score*1),green,750,10)
            text_screen('Highscore: '+str(highscore),red,710,40)
            pygame.draw.rect(gamewindow,blue,[snake_x,snake_y,snake_size,snake_size])
            head = []
            head.append(snake_x)
            head.append(snake_y)

            if len(snk_list)> snk_length:
                del snk_list[0]
            if snake_x >= screen_width or snake_y >= screen_height:
                gameov.play()
                game_over = True
                time.sleep(1)
                
            if snake_x < 0 or snake_y < 0:
                gameov.play()
                game_over = True
                time.sleep(1)

            if head in snk_list[:-1]:
                game_over= True
                time.sleep(1)


            plot_snake(gamewindow,blue,snk_list,snake_size)
            
            snk_list.append(head)
            pygame.draw.rect(gamewindow,red,[food_x,food_y,food_size,food_size])
        pygame.display.update()
        clock.tick(fps)
    

    pygame.quit()
    sys.exit()

welcome()
gameloop()
