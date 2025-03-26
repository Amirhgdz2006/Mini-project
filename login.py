import pygame
import hashpassword
from pygame.locals import * #keydown , key_backspace , quite va ...
import game
import subprocess
import sys

pygame.init()

#in tabe kilid migire az karbar va hamono barmigrdone va agar karbar zarbdar ro bezane kolan miad biron az game
def gerftan_key_khoroj():
    while True:
        event = pygame.event.wait()
        if event.type == KEYDOWN:
            return event.key
        elif event.type == QUIT:
            pygame.quit()
            sys.exit()

#matn safahat ro ba tamami joziiat amade mikne
def matn_safe_siah(screen, message, x=0, y=0):
    font_text = pygame.font.Font(None , 24)
    range_text = font_text.render(message, True ,(255, 255, 255))
    mostatil_text = range_text.get_rect(center=((screen.get_width() / 2) + x, (screen.get_height() / 2) + y))
    pygame.draw.rect(screen, (0, 0, 0), mostatil_text.inflate(10, 10))
    pygame.draw.rect(screen, (255, 255, 255), mostatil_text.inflate(12, 12), 1)
    screen.blit(range_text, mostatil_text)

#bozorg va kuchiki va darvaghe barresi kardn va ezafe kardn vorodi haye karbar
def vorodiha(screen, question, x=0, y=0):
    pygame.font.init() #bug
    matn_halehazer = []
    shift_pressed = False 
    screen.fill((50, 50, 50)) #rang asli safe
    matn_safe_siah(screen, question + ": " + ''.join(matn_halehazer), x, y)
    pygame.display.update()
    
    while True:
        vorodie = gerftan_key_khoroj()
        
        if vorodie == K_BACKSPACE:
            matn_halehazer = matn_halehazer[:-1]
        elif vorodie == K_RETURN:
            break
        elif vorodie in (K_LSHIFT, K_RSHIFT , K_CAPSLOCK):
            # shift_pressed = True
            shift_pressed = not shift_pressed
            continue
        elif shift_pressed and 97 <= vorodie <= 122:  
            matn_halehazer.append(chr(vorodie - 32)) 
            # shift_pressed = False
 
        elif 32 <= vorodie <= 126: 
            matn_halehazer.append(chr(vorodie))
        screen.fill((50, 50, 50))
        matn_safe_siah(screen, question + ": " + ''.join(matn_halehazer), x, y)
        pygame.display.update()
    
    return ''.join(matn_halehazer)

def menu_aval(screen):
    while True:
        screen.fill((50, 50, 50))
        matn_safe_siah(screen, "Press 1 to Play Game", 0, -30)
        matn_safe_siah(screen, "Press 2 for Leaderboard", 0, 30)
        pygame.display.update()
        
        key = gerftan_key_khoroj()
        if key == K_1:
            return "play"
        elif key == K_2:
            return "leaderboard"

#agar player play ro zad
def login_menu(screen):
    screen.fill((50, 50, 50))
    matn_safe_siah(screen, "Press 1 for Sign Up", 0 , -30)
    matn_safe_siah(screen, "Press 2 for Login", 0 , 30)
    pygame.display.update()
    
    while True:
        key = gerftan_key_khoroj()
        if key == K_1:
            return "signup"
        elif key == K_2:
            return "login"

#nahve vorod player
def player_login(screen, player):
    while True:
        screen.fill((50, 50, 50))
        # matn_safe_siah(screen, f"{player} Turn" , 0 , 0)
        pygame.display.update()
        choice = login_menu(screen)
        username = vorodiha(screen, "Username", 0, -30)
        password = vorodiha(screen, "Password", 0, 30)
        
        if choice == "signup":
            if hashpassword.add_user(username, password):
                matn_safe_siah(screen, f"{username} registered!", 0, 90)
                pygame.display.update()
                pygame.time.wait(2000)
                return username
            else:
                matn_safe_siah(screen, f"{username} already exists!", 0, 90)
                pygame.display.update()
                pygame.time.wait(2000)
        elif choice == "login":
            result = hashpassword.check_password(username, password)
            if result == "not_found":
                matn_safe_siah(screen, f"{username} not found!", 0, 90)
            elif result:
                matn_safe_siah(screen, f"{username} logged in!", 0, 90)
                pygame.display.update()
                pygame.time.wait(2000)
                return username
            else:
                matn_safe_siah(screen, "Wrong password!", 0, 90)
            pygame.display.update()
            pygame.time.wait(2000)

def main():
    screen = pygame.display.set_mode((500, 500))
    choice = menu_aval(screen)
    
    if choice == "play":
        player1_username = player_login(screen, "Player 1")
        player2_username = player_login(screen, "Player 2")
        game.run_game(player1_username, player2_username)

    elif choice == "leaderboard":
        subprocess.run(["python", "leaderboard.py"])
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()