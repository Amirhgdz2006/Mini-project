import pygame as pg
from pygame.locals import *
import random
import copy
import math
import hashpassword
import subprocess
import time

pg.init()



class dartboard:
    def __init__(self):
        self.x = random.randint(25, 975)
        self.y = random.randint(25, 575)
        self.r = 25
        

class timeboard:
    def __init__(self):
        self.x = random.randint(25, 975)
        self.y = random.randint(25, 575)
        self.r = 15

class bulletboard:
    def __init__(self):
        self.x = random.randint(25, 975)
        self.y = random.randint(25, 575)
        self.r = 15

class player:
    def __init__(self, username):
        self.username = username
        self.score = 0
        self.bullet = 10
        self.time = 7200

def changing(class_name, lst_bullet_blue_temp, lst_bullet_red_temp):
    i = random.randint(25, 975)
    j = random.randint(25, 575)
    while (math.sqrt(float(lst_bullet_blue_temp[0][0]-i)**2 + float(lst_bullet_blue_temp[0][1]-j)**2) <= float(15)) and \
          (math.sqrt(float(lst_bullet_red_temp[0][0]-i)**2 + float(lst_bullet_red_temp[0][1]-j)**2) <= float(15)):
        i = random.randint(25, 975)
        j = random.randint(25, 575)
    class_name.x = i
    class_name.y = j

def run_game(player1_username, player2_username):
    screen = pg.display.set_mode([1140, 600])
    pygame_icon = pg.image.load('gameicon.png')
    pg.display.set_icon(pygame_icon)

    dartboard_1 = dartboard()
    dartboard_2 = dartboard()
    dartboard_3 = dartboard()
    timeboard_1 = timeboard()
    bulletboard_1 = bulletboard()

    player_1 = player(player1_username)
    player_2 = player(player2_username)

    lst_bullet_blue = []
    lst_bullet_blue_temp = []
    lst_bullet_red = []
    lst_bullet_red_temp = []

    is_running = True
    first_move_blue = True
    first_move_red = True
    game_end = False

    fps = pg.time.Clock()
    font = pg.font.SysFont('Arial', 18)
    font2 = pg.font.SysFont('Arial', 80)
    font3 = pg.font.SysFont('Arial', 16)
    lst_notif = ['']

    dart_icon = pg.image.load('dart.png')
    dart_icon = pg.transform.scale(dart_icon , [50,50])

    bullet_icon = pg.image.load('bullet.png')
    bullet_icon = pg.transform.scale(bullet_icon , [30,30])

    time_icon = pg.image.load('time.png')
    time_icon = pg.transform.scale(time_icon , [30,30])

    while is_running:
        screen.fill('white')
        pg.draw.rect(screen, 'gray', [1000, 0, 140, 600])

        player_1_text = font.render(f'{player_1.username}:', True, 'black')
        player_1_score_text = font.render(f'score: {player_1.score}', True, 'black')
        player_1_bullet_text = font.render(f'bullet: {player_1.bullet}', True, 'black')
        player_1_time_text = font.render(f'time: {round(float(player_1.time/60), 2)}', True, 'black')
        
        player_2_text = font.render(f'{player_2.username}:', True, 'black')
        player_2_score_text = font.render(f'score: {player_2.score}', True, 'black')
        player_2_bullet_text = font.render(f'bullet: {player_2.bullet}', True, 'black')
        player_2_time_text = font.render(f'time: {round(float(player_2.time/60), 2)}', True, 'black')
        
        screen.blit(player_1_text, (1010, 20))
        screen.blit(player_1_score_text, (1010, 60))
        screen.blit(player_1_bullet_text, (1010, 100))
        screen.blit(player_1_time_text, (1010, 140))
        
        screen.blit(player_2_text, (1010, 300))
        screen.blit(player_2_score_text, (1010, 340))
        screen.blit(player_2_bullet_text, (1010, 380))
        screen.blit(player_2_time_text, (1010, 420))

        pg.draw.rect(screen, 'gray', [1000, 500, 100, 100])
        notif_text = font3.render(f'{lst_notif[-1]}', True, 'black')
        screen.blit(notif_text, (1005, 501))

        # pg.draw.circle(screen, 'green', (dartboard_1.x, dartboard_1.y), dartboard_1.r)
        screen.blit(dart_icon,(dartboard_1.x-25, dartboard_1.y-25))
        # pg.draw.circle(screen, 'green', (dartboard_2.x, dartboard_2.y), dartboard_2.r)
        screen.blit(dart_icon,(dartboard_2.x-25, dartboard_2.y-25))
        # pg.draw.circle(screen, 'green', (dartboard_3.x, dartboard_3.y), dartboard_3.r)
        screen.blit(dart_icon,(dartboard_3.x-25, dartboard_3.y-25))
        # pg.draw.circle(screen, 'purple', (timeboard_1.x, timeboard_1.y), timeboard_1.r)
        screen.blit(time_icon,(timeboard_1.x-15, timeboard_1.y-15))
        # pg.draw.circle(screen, 'orange', (bulletboard_1.x, bulletboard_1.y), bulletboard_1.r)
        screen.blit(bullet_icon,(bulletboard_1.x-15, bulletboard_1.y-15))

        for coordinate in lst_bullet_blue:
            if lst_bullet_blue.index(coordinate) == len(lst_bullet_blue)-1:
                pg.draw.circle(screen, '#00308F', (coordinate[0], coordinate[1]), 5)
            else:
                pg.draw.circle(screen, '#7CB9E8', (coordinate[0], coordinate[1]), 5)

        for coordinate in lst_bullet_red:
            if lst_bullet_red.index(coordinate) == len(lst_bullet_red)-1:
                pg.draw.circle(screen, '#AA0000', (coordinate[0], coordinate[1]), 5)
            else:
                pg.draw.circle(screen, '#fd5c63', (coordinate[0], coordinate[1]), 5)

        if not game_end:
            if player_1.time > 0:
                player_1.time -= 1
            else:
                player_1.time = 0
            if player_2.time > 0:
                player_2.time -= 1
            else:
                player_2.time = 0

        for item in pg.event.get():
            if item.type == QUIT:
                is_running = False
                break

            if item.type == KEYDOWN and player_1.bullet > 0 and player_1.time > 0:
                if first_move_blue and item.key == K_SPACE:
                    lst_bullet_blue.append([random.randint(5, 995), random.randint(5, 595)])
                    lst_bullet_blue_temp = copy.deepcopy(lst_bullet_blue)
                    first_move_blue = False
                elif not first_move_blue and not game_end:
                    if item.key == K_UP and lst_bullet_blue_temp[0][1] > 10:
                        lst_bullet_blue_temp[0][1] -= 10
                    elif item.key == K_RIGHT and lst_bullet_blue_temp[0][0] < 990:
                        lst_bullet_blue_temp[0][0] += 10
                    elif item.key == K_DOWN and lst_bullet_blue_temp[0][1] < 590:
                        lst_bullet_blue_temp[0][1] += 10
                    elif item.key == K_LEFT and lst_bullet_blue_temp[0][0] > 10:
                        lst_bullet_blue_temp[0][0] -= 10
                    elif item.key == K_RSHIFT:
                        lst_bullet_blue.append(copy.deepcopy(lst_bullet_blue_temp[0]))
                        player_1.bullet -= 1 if player_1.bullet > 0 else 0

                        if math.sqrt((lst_bullet_blue_temp[0][0] - dartboard_1.x)**2 + (lst_bullet_blue_temp[0][1] - dartboard_1.y)**2) <= dartboard_1.r:
                            changing(dartboard_1, lst_bullet_blue_temp, lst_bullet_red_temp)
                            player_1.score += 1
                            lst_notif.append(f'{player_1.username} hit the target')
                        elif math.sqrt((lst_bullet_blue_temp[0][0] - dartboard_2.x)**2 + (lst_bullet_blue_temp[0][1] - dartboard_2.y)**2) <= dartboard_2.r:
                            changing(dartboard_2, lst_bullet_blue_temp, lst_bullet_red_temp)
                            player_1.score += 1
                            lst_notif.append(f'{player_1.username} hit the target')
                        elif math.sqrt((lst_bullet_blue_temp[0][0] - dartboard_3.x)**2 + (lst_bullet_blue_temp[0][1] - dartboard_3.y)**2) <= dartboard_3.r:
                            changing(dartboard_3, lst_bullet_blue_temp, lst_bullet_red_temp)
                            player_1.score += 1
                            lst_notif.append(f'{player_1.username} hit the target')
                        elif math.sqrt((lst_bullet_blue_temp[0][0] - timeboard_1.x)**2 + (lst_bullet_blue_temp[0][1] - timeboard_1.y)**2) <= timeboard_1.r:
                            changing(timeboard_1, lst_bullet_blue_temp, lst_bullet_red_temp)
                            player_1.time += 1800
                            lst_notif.append(f'{player_1.username} time added')
                        elif math.sqrt((lst_bullet_blue_temp[0][0] - bulletboard_1.x)**2 + (lst_bullet_blue_temp[0][1] - bulletboard_1.y)**2) <= bulletboard_1.r:
                            changing(bulletboard_1, lst_bullet_blue_temp, lst_bullet_red_temp)
                            player_1.bullet += 5
                            lst_notif.append(f'{player_1.username} bullet added')

            if item.type == KEYDOWN and player_2.bullet > 0 and player_2.time > 0:
                if first_move_red and item.key == K_SPACE:
                    lst_bullet_red.append([random.randint(5, 995), random.randint(5, 595)])
                    lst_bullet_red_temp = copy.deepcopy(lst_bullet_red)
                    first_move_red = False
                elif not first_move_red and not game_end:
                    if item.key == K_w and lst_bullet_red_temp[0][1] > 10:
                        lst_bullet_red_temp[0][1] -= 10
                    elif item.key == K_d and lst_bullet_red_temp[0][0] < 990:
                        lst_bullet_red_temp[0][0] += 10
                    elif item.key == K_s and lst_bullet_red_temp[0][1] < 590:
                        lst_bullet_red_temp[0][1] += 10
                    elif item.key == K_a and lst_bullet_red_temp[0][0] > 10:
                        lst_bullet_red_temp[0][0] -= 10
                    elif item.key == K_LSHIFT:
                        lst_bullet_red.append(copy.deepcopy(lst_bullet_red_temp[0]))
                        player_2.bullet -= 1 if player_2.bullet > 0 else 0

                        if math.sqrt((lst_bullet_red_temp[0][0] - dartboard_1.x)**2 + (lst_bullet_red_temp[0][1] - dartboard_1.y)**2) <= dartboard_1.r:
                            changing(dartboard_1, lst_bullet_blue_temp, lst_bullet_red_temp)
                            player_2.score += 1
                            lst_notif.append(f'{player_2.username} hit the target')
                        elif math.sqrt((lst_bullet_red_temp[0][0] - dartboard_2.x)**2 + (lst_bullet_red_temp[0][1] - dartboard_2.y)**2) <= dartboard_2.r:
                            changing(dartboard_2, lst_bullet_blue_temp, lst_bullet_red_temp)
                            player_2.score += 1
                            lst_notif.append(f'{player_2.username} hit the target')
                        elif math.sqrt((lst_bullet_red_temp[0][0] - dartboard_3.x)**2 + (lst_bullet_red_temp[0][1] - dartboard_3.y)**2) <= dartboard_3.r:
                            changing(dartboard_3, lst_bullet_blue_temp, lst_bullet_red_temp)
                            player_2.score += 1
                            lst_notif.append(f'{player_2.username} hit the target')
                        elif math.sqrt((lst_bullet_red_temp[0][0] - timeboard_1.x)**2 + (lst_bullet_red_temp[0][1] - timeboard_1.y)**2) <= timeboard_1.r:
                            changing(timeboard_1, lst_bullet_blue_temp, lst_bullet_red_temp)
                            player_2.time += 1800
                            lst_notif.append(f'{player_2.username} time added')
                        elif math.sqrt((lst_bullet_red_temp[0][0] - bulletboard_1.x)**2 + (lst_bullet_red_temp[0][1] - bulletboard_1.y)**2) <= bulletboard_1.r:
                            changing(bulletboard_1, lst_bullet_blue_temp, lst_bullet_red_temp)
                            player_2.bullet += 5
                            lst_notif.append(f'{player_2.username} bullet added')

        player_1_win = font2.render(f'{player_1.username} WINS', True, 'yellow')
        player_2_win = font2.render(f'{player_2.username} WINS', True, 'yellow')
        draw = font2.render('Draw', True, 'yellow')

        if (player_1.bullet == 0 and player_2.bullet == 0) or (player_1.time <= 0 and player_2.time <= 0):
            game_end = True


            if player_1.score > player_2.score:
                screen.blit(player_1_win, (300, 220))
                hashpassword.update_game_result(player_1.username, player_1.score, "win")
                hashpassword.update_game_result(player_2.username, player_2.score, "lose")
                

                
            elif player_1.score < player_2.score:
                screen.blit(player_2_win, (300, 220))
                hashpassword.update_game_result(player_1.username, player_1.score, "lose")
                hashpassword.update_game_result(player_2.username, player_2.score, "win")


            else:
                screen.blit(draw, (450, 220))
                hashpassword.update_game_result(player_1.username, player_1.score, "draw")
                hashpassword.update_game_result(player_2.username, player_2.score, "draw")
        

        if game_end:

            pg.display.update()
            time.sleep(5)  
            break

        pg.display.update()
        fps.tick(60)



    pg.quit()

if __name__ == '__main__':
    subprocess.run(["python", "login.py"])
    run_game()