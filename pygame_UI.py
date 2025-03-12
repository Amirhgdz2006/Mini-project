# ---------------------------------------- import and (init)
import pygame as pg
from pygame.locals import *
import random
import sys
import copy
import math

pg.init()
# ---------------------------------------- class
class dartboard:
    def __init__(self):
        self.x = random.randint(25,975)
        self.y = random.randint(25,575)
        self.r = 25

dartboard_1 = dartboard()
dartboard_2 = dartboard()
dartboard_3 = dartboard()

class player:
    def __init__(self):
        self.score = 0
        self.bullet = 10
        self.time = 7200
        # (120)(time limit) * 60(fps)


player_1 = player()
player_2 = player()
# ---------------------------------------- def 
def changing(class_name):
    class_name.x = random.randint(25,975)
    class_name.y = random.randint(25,975)
# ---------------------------------------- pygame (UI)
screen = pg.display.set_mode([1100, 600])

pygame_icon = pg.image.load('image-logo/game_icon.png')
pg.display.set_icon(pygame_icon)

lst_bullet_blue = []
lst_bullet_blue_temp = []

lst_bullet_red = []
lst_bullet_red_temp = []
# -------------------- loop
# trun 1 --> blue  , turn 2 --> red    
is_running = True
first_move_blue = True
first_move_red = True
turn = 1
fps = pg.time.Clock()

font = pg.font.SysFont('Arial',20)
font2 = pg.font.SysFont('Arial',80)

while is_running:
    # ---------- screen
    screen.fill('white')

    pg.draw.rect(screen,'gray',[1000,0,100,600])

    
    player_1_text = font.render('player 1 :',True,'black')
    player_1_score_text = font.render(f'score : {player_1.score}',True,'black')
    player_1_bullet_text = font.render(f'bullet : {player_1.bullet}',True,'black')
    player_1_time_text = font.render(f'time : {float(player_1.time/60)}',True,'black')
    
    player_2_text = font.render('player 2 :',True,'black')
    player_2_score_text = font.render(f'score : {player_2.score}',True,'black')
    player_2_bullet_text = font.render(f'bullet : {player_2.bullet}',True,'black')
    player_2_time_text = font.render(f'time : {float(player_2.time/60)}',True,'black')
    
    screen.blit(player_1_text,(1010,20))
    screen.blit(player_1_score_text,(1010,60))
    screen.blit(player_1_bullet_text,(1010,100))
    screen.blit(player_1_time_text,(1010,140))
    
    screen.blit(player_2_text,(1010,300))
    screen.blit(player_2_score_text,(1010,340))
    screen.blit(player_2_bullet_text,(1010,380))
    screen.blit(player_2_time_text,(1010,420))
    # ----------

    # ---------- dartboard
    pg.draw.circle(screen,'green',(dartboard_1.x,dartboard_1.y),dartboard_1.r)
    pg.draw.circle(screen,'green',(dartboard_2.x,dartboard_2.y),dartboard_2.r)
    pg.draw.circle(screen,'green',(dartboard_3.x,dartboard_3.y),dartboard_3.r)
    # ----------

    # ---------- pointer
    for coordinate in lst_bullet_blue:
        pg.draw.circle(screen, 'blue', (coordinate[0], coordinate[1]), 5)

    for coordinate in lst_bullet_red:
        pg.draw.circle(screen, 'red', (coordinate[0], coordinate[1]), 5)
    # ----------

    if turn == 1:
        if int(player_1.time) > 0:
            player_1.time -= 1
        else:
            player_1.time = 0

    elif turn == 2:
        if int(player_2.time) > 0:
            player_2.time -= 1
        else:
            player_2.time = 0

    for item in pg.event.get():
        
        if item.type == QUIT:
            is_running = False
            break  

        if turn == 1:

            if item.type == KEYDOWN:

                if first_move_blue == True:
                    if item.key == K_SPACE:
                        lst_bullet_blue.append([random.randint(5, 995), random.randint(5, 595)])
                        lst_bullet_blue_temp = copy.deepcopy(lst_bullet_blue)
                        first_move_blue = False

                if first_move_blue == False: 


                    if item.key == K_UP:
                        lst_bullet_blue_temp[0][1] -= 10
                        
                    elif item.key == K_RIGHT:
                        lst_bullet_blue_temp[0][0] += 10

                    elif item.key == K_DOWN:
                        lst_bullet_blue_temp[0][1] += 10

                    elif item.key == K_LEFT:
                        lst_bullet_blue_temp[0][0] -= 10

                    if item.key == K_SPACE:
                        lst_bullet_blue.append(copy.deepcopy(lst_bullet_blue_temp[0]))
                        player_1.bullet -= 1

                        # ---------- checking
                        if math.sqrt(float(lst_bullet_blue_temp[0][0]-dartboard_1.x)**2 + float(lst_bullet_blue_temp[0][1]-dartboard_1.y)**2) <= float(dartboard_1.r):
                            changing(dartboard_1)
                            player_1.score += 1

                        elif math.sqrt(float(lst_bullet_blue_temp[0][0]-dartboard_2.x)**2 + float(lst_bullet_blue_temp[0][1]-dartboard_2.y)**2) <= float(dartboard_2.r):
                            changing(dartboard_2)
                            player_1.score += 1

                        elif math.sqrt(float(lst_bullet_blue_temp[0][0]-dartboard_3.x)**2 + float(lst_bullet_blue_temp[0][1]-dartboard_3.y)**2) <= float(dartboard_3.r):
                            changing(dartboard_3)
                            player_1.score += 1

                        # ----------
                        if int(player_2.time) != 0:
                            turn = 2



        elif turn == 2:

            if item.type == KEYDOWN:

                if first_move_red == True:
                    if item.key == K_SPACE:
                        lst_bullet_red.append([random.randint(5, 995), random.randint(5, 595)])
                        lst_bullet_red_temp = copy.deepcopy(lst_bullet_red)
                        first_move_red = False

                if first_move_red == False: 
                
                
                    if item.key == K_UP:
                        lst_bullet_red_temp[0][1] -= 10
                        
                    elif item.key == K_RIGHT:
                        lst_bullet_red_temp[0][0] += 10

                    elif item.key == K_DOWN:
                        lst_bullet_red_temp[0][1] += 10
                    elif item.key == K_LEFT:
                        lst_bullet_red_temp[0][0] -= 10

                    if item.key == K_SPACE:
                        lst_bullet_red.append(copy.deepcopy(lst_bullet_red_temp[0]))
                        player_2.bullet -= 1

                        # ---------- checking
                        if math.sqrt(float(lst_bullet_red_temp[0][0]-dartboard_1.x)**2 + float(lst_bullet_red_temp[0][1]-dartboard_1.y)**2) <= float(dartboard_1.r):
                            changing(dartboard_1)
                            player_2.score += 1

                        elif math.sqrt(float(lst_bullet_red_temp[0][0]-dartboard_2.x)**2 + float(lst_bullet_red_temp[0][1]-dartboard_2.y)**2) <= float(dartboard_2.r):
                            changing(dartboard_2)
                            player_2.score += 1

                        elif math.sqrt(float(lst_bullet_red_temp[0][0]-dartboard_3.x)**2 + float(lst_bullet_red_temp[0][1]-dartboard_3.y)**2) <= float(dartboard_3.r):
                            changing(dartboard_3)
                            player_2.score += 1
                        # ----------
                        if int(player_1.time) != 0:
                            turn = 1

    player_1_win = font2.render('Player 1 WIN',True,'yellow')
    player_2_win = font2.render('Player 2 WIN',True,'yellow')
    draw = font2.render('Draw',True,'yellow')

    if player_1.bullet == 0 and player_2.bullet == 0:
        if player_1.score > player_2.score:
            screen.blit(player_1_win,(300,200))

        elif player_1.score == player_2.score:
            screen.blit(draw,(300,200))

        elif player_1.score < player_2.score:
            screen.blit(player_2_win,(300,200))


    if int(player_1.time) <= 0 and int(player_2.time) <= 0:
        if player_1.score > player_2.score:
            screen.blit(player_1_win,((300,200)))

        elif player_1.score == player_2.score:
            screen.blit(draw,(300,200))

        elif player_1.score < player_2.score:
            screen.blit(player_2_win,(300,200))

    pg.display.update()
    fps.tick(60)

pg.quit()
sys.exit()



