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

class timeboard:
    
    def __init__(self):
        self.x = random.randint(25,975)
        self.y = random.randint(25,575)
        self.r = 15

timeboard_1 = timeboard()

class bulletboard:
    
    def __init__(self):
        self.x = random.randint(25,975)
        self.y = random.randint(25,575)
        self.r = 15

bulletboard_1 = bulletboard()

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
    i = random.randint(25,975)
    j = random.randint(25,575)
    while (math.sqrt(float(lst_bullet_blue_temp[0][0]-i)**2 + float(lst_bullet_blue_temp[0][1]-j)**2) <= float(15)) and (math.sqrt(float(lst_bullet_red_temp[0][0]-i)**2 + float(lst_bullet_red_temp[0][1]-j)**2) <= float(15)):
        i = random.randint(25,975)
        j = random.randint(25,575)
    class_name.x = i
    class_name.y = j
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
game_end = False

fps = pg.time.Clock()

font = pg.font.SysFont('Arial',18)
font2 = pg.font.SysFont('Arial',80)
font3 = pg.font.SysFont('Arial',13)

lst_notif = ['']


while is_running:
    # ---------- screen
    screen.fill('white')

    pg.draw.rect(screen,'gray',[1000,0,100,600])

    
    player_1_text = font.render('player 1 :',True,'black')
    player_1_score_text = font.render(f'score : {player_1.score}',True,'black')
    player_1_bullet_text = font.render(f'bullet : {player_1.bullet}',True,'black')
    player_1_time_text = font.render(f'time : {round(float(player_1.time/60),2)}',True,'black')
    
    player_2_text = font.render('player 2 :',True,'black')
    player_2_score_text = font.render(f'score : {player_2.score}',True,'black')
    player_2_bullet_text = font.render(f'bullet : {player_2.bullet}',True,'black')
    player_2_time_text = font.render(f'time : {round(float(player_2.time/60),2)}',True,'black')
    
    screen.blit(player_1_text,(1010,20))
    screen.blit(player_1_score_text,(1010,60))
    screen.blit(player_1_bullet_text,(1010,100))
    screen.blit(player_1_time_text,(1010,140))
    
    screen.blit(player_2_text,(1010,300))
    screen.blit(player_2_score_text,(1010,340))
    screen.blit(player_2_bullet_text,(1010,380))
    screen.blit(player_2_time_text,(1010,420))

    pg.draw.rect(screen,'gray',[1000,500,100,100])
    notif_text = font3.render(f'{lst_notif[-1]}',True,'black')
    screen.blit(notif_text,(1001,501))
    # ----------

    # ---------- dartboard ---> green
    pg.draw.circle(screen,'green',(dartboard_1.x,dartboard_1.y),dartboard_1.r)
    pg.draw.circle(screen,'green',(dartboard_2.x,dartboard_2.y),dartboard_2.r)
    pg.draw.circle(screen,'green',(dartboard_3.x,dartboard_3.y),dartboard_3.r)
    # ----------

    # ---------- timeboard ---> purple
    pg.draw.circle(screen,'purple',(timeboard_1.x,timeboard_1.y),timeboard_1.r)
    # ----------

    # ---------- bulletboard ---> orange
    pg.draw.circle(screen,'orange',(bulletboard_1.x,bulletboard_1.y),bulletboard_1.r)
    # ----------

    # ---------- pointer
    for coordinate in lst_bullet_blue:
        pg.draw.circle(screen, 'blue', (coordinate[0], coordinate[1]), 5)

    for coordinate in lst_bullet_red:
        pg.draw.circle(screen, 'red', (coordinate[0], coordinate[1]), 5)
    # ----------

    
    if game_end == False:
        if int(player_1.time) > 0:
            player_1.time -= 1
        else:
            player_1.time = 0

    
    if game_end == False:
        if int(player_2.time) > 0:
            player_2.time -= 1
        else:
            player_2.time = 0


    for item in pg.event.get():
        
        if item.type == QUIT:
            is_running = False
            break  

        

        if item.type == KEYDOWN:
            if player_1.bullet > 0 and player_1.time > 0 :

                if first_move_blue == True:
                    if item.key == K_SPACE:
                        lst_bullet_blue.append([random.randint(5, 995), random.randint(5, 595)])
                        lst_bullet_blue_temp = copy.deepcopy(lst_bullet_blue)
                        first_move_blue = False

                if first_move_blue == False: 
                    
                    if game_end == False:

                        if item.key == K_UP:
                            if lst_bullet_blue_temp[0][1] > 10:
                                lst_bullet_blue_temp[0][1] -= 10
                            
                        elif item.key == K_RIGHT:
                            if lst_bullet_blue_temp[0][0] < 990:
                                lst_bullet_blue_temp[0][0] += 10

                        elif item.key == K_DOWN:
                            if lst_bullet_blue_temp[0][1] < 590:
                                lst_bullet_blue_temp[0][1] += 10

                        elif item.key == K_LEFT:
                            if lst_bullet_blue_temp[0][0] > 10:
                                lst_bullet_blue_temp[0][0] -= 10

                        if item.key ==  K_RSHIFT:
                            lst_bullet_blue.append(copy.deepcopy(lst_bullet_blue_temp[0]))
                            if player_1.bullet > 0:
                                player_1.bullet -= 1
                            else:
                                player_1.bullet = 0

                            # ---------- checking
                            if math.sqrt(float(lst_bullet_blue_temp[0][0]-dartboard_1.x)**2 + float(lst_bullet_blue_temp[0][1]-dartboard_1.y)**2) <= float(dartboard_1.r):
                                changing(dartboard_1)
                                player_1.score += 1
                                lst_notif.append('player 1 hit the taget')

                            elif math.sqrt(float(lst_bullet_blue_temp[0][0]-dartboard_2.x)**2 + float(lst_bullet_blue_temp[0][1]-dartboard_2.y)**2) <= float(dartboard_2.r):
                                changing(dartboard_2)
                                player_1.score += 1
                                lst_notif.append('player 1 hit the taget')

                            elif math.sqrt(float(lst_bullet_blue_temp[0][0]-dartboard_3.x)**2 + float(lst_bullet_blue_temp[0][1]-dartboard_3.y)**2) <= float(dartboard_3.r):
                                changing(dartboard_3)
                                player_1.score += 1
                                lst_notif.append('player 1 hit the taget')

                            elif math.sqrt(float(lst_bullet_blue_temp[0][0]-timeboard_1.x)**2 + float(lst_bullet_blue_temp[0][1]-timeboard_1.y)**2) <= float(timeboard_1.r):
                                changing(timeboard_1)
                                player_1.time += 1800
                                lst_notif.append('player 1 time added')


                            elif math.sqrt(float(lst_bullet_blue_temp[0][0]-bulletboard_1.x)**2 + float(lst_bullet_blue_temp[0][1]-bulletboard_1.y)**2) <= float(bulletboard_1.r):
                                changing(bulletboard_1)
                                player_1.bullet += 5
                                lst_notif.append('player 1 bullet added')

                        # ----------




        

        if item.type == KEYDOWN:
            if player_2.bullet > 0 and player_2.time > 0:

                if first_move_red == True:
                    if item.key == K_SPACE:
                        lst_bullet_red.append([random.randint(5, 995), random.randint(5, 595)])
                        lst_bullet_red_temp = copy.deepcopy(lst_bullet_red)
                        first_move_red = False

                if first_move_red == False: 
                    
                    if game_end == False:
                
                        if item.key == K_w:
                            if lst_bullet_red_temp[0][1] > 10:
                                lst_bullet_red_temp[0][1] -= 10
                            
                        elif item.key == K_d:
                            if lst_bullet_red_temp[0][0] < 990:
                                lst_bullet_red_temp[0][0] += 10

                        elif item.key == K_s:
                            if lst_bullet_red_temp[0][1] < 590:
                                lst_bullet_red_temp[0][1] += 10

                        elif item.key == K_a:
                            if lst_bullet_red_temp[0][0] > 10:
                                lst_bullet_red_temp[0][0] -= 10

                        if item.key == K_LSHIFT :
                            lst_bullet_red.append(copy.deepcopy(lst_bullet_red_temp[0]))
                            if player_2.bullet > 0:
                                player_2.bullet -= 1
                            else:
                                player_2.bullet = 0

                            # ---------- checking
                            if math.sqrt(float(lst_bullet_red_temp[0][0]-dartboard_1.x)**2 + float(lst_bullet_red_temp[0][1]-dartboard_1.y)**2) <= float(dartboard_1.r):
                                changing(dartboard_1)
                                player_2.score += 1
                                lst_notif.append('player 2 hit the taget')

                            elif math.sqrt(float(lst_bullet_red_temp[0][0]-dartboard_2.x)**2 + float(lst_bullet_red_temp[0][1]-dartboard_2.y)**2) <= float(dartboard_2.r):
                                changing(dartboard_2)
                                player_2.score += 1
                                lst_notif.append('player 2 hit the taget')

                            elif math.sqrt(float(lst_bullet_red_temp[0][0]-dartboard_3.x)**2 + float(lst_bullet_red_temp[0][1]-dartboard_3.y)**2) <= float(dartboard_3.r):
                                changing(dartboard_3)
                                player_2.score += 1
                                lst_notif.append('player 2 hit the taget')


                            elif math.sqrt(float(lst_bullet_red_temp[0][0]-timeboard_1.x)**2 + float(lst_bullet_red_temp[0][1]-timeboard_1.y)**2) <= float(timeboard_1.r):
                                changing(timeboard_1)
                                player_2.time += 1800
                                lst_notif.append('player 2 time added')

                            elif math.sqrt(float(lst_bullet_red_temp[0][0]-bulletboard_1.x)**2 + float(lst_bullet_red_temp[0][1]-bulletboard_1.y)**2) <= float(bulletboard_1.r):
                                changing(bulletboard_1)
                                player_2.bullet += 5
                                lst_notif.append('player 2 bullet added')
                        # ----------


    player_1_win = font2.render('Player 1 WIN',True,'yellow')
    player_2_win = font2.render('Player 2 WIN',True,'yellow')
    draw = font2.render('Draw',True,'yellow')

    if player_1.bullet == 0 and player_2.bullet == 0:
        if player_1.score > player_2.score:
            screen.blit(player_1_win,(300,220))

        elif player_1.score == player_2.score:
            screen.blit(draw,(450,220))

        elif player_1.score < player_2.score:
            screen.blit(player_2_win,(300,220))


        game_end = True


    if int(player_1.time) <= 0 and int(player_2.time) <= 0:
        if player_1.score > player_2.score:
            screen.blit(player_1_win,((300,220)))

        elif player_1.score == player_2.score:
            screen.blit(draw,(450,220))

        elif player_1.score < player_2.score:
            screen.blit(player_2_win,(300,220))

        game_end = True

    pg.display.update()
    fps.tick(60)

pg.quit()
sys.exit()



