import pygame
import hashpassword
from pygame.locals import *
import pygame_UI
import subprocess
import sys

pygame.init()

def get_key():
    while True:
        event = pygame.event.wait()
        if event.type == KEYDOWN:
            return event.key
        elif event.type == QUIT:
            pygame.quit()
            sys.exit()

def safe_siah(screen, message, x=0, y=0):
    fontobject = pygame.font.Font(None, 24)
    text_surface = fontobject.render(message, True, (255, 255, 255))
    text_rect = text_surface.get_rect(center=((screen.get_width() / 2) + x, (screen.get_height() / 2) + y))
    pygame.draw.rect(screen, (0, 0, 0), text_rect.inflate(10, 10))
    pygame.draw.rect(screen, (255, 255, 255), text_rect.inflate(12, 12), 1)
    screen.blit(text_surface, text_rect)

def vorodiha(screen, question, x=0, y=0):
    pygame.font.init()
    current_string = []
    shift_pressed = False 
    screen.fill((50, 50, 50))
    safe_siah(screen, question + ": " + ''.join(current_string), x, y)
    pygame.display.update()
    
    while True:
        inkey = get_key()
        
        if inkey == K_BACKSPACE:
            current_string = current_string[:-1]
        elif inkey == K_RETURN:
            break
        elif inkey in (K_LSHIFT, K_RSHIFT): 
            shift_pressed = True
            continue
        elif shift_pressed and 97 <= inkey <= 122:  
            current_string.append(chr(inkey - 32))  
            shift_pressed = False
        elif 32 <= inkey <= 126: 
            current_string.append(chr(inkey))
        
        screen.fill((50, 50, 50))
        safe_siah(screen, question + ": " + ''.join(current_string), x, y)
        pygame.display.update()
    
    return ''.join(current_string)

def menu_aval(screen):
    while True:
        screen.fill((50, 50, 50))
        safe_siah(screen, "Press 1 to Play Game", 0, -30)
        safe_siah(screen, "Press 2 for Leaderboard", 0, 30)
        pygame.display.update()
        
        key = get_key()
        if key == K_1:
            return "play"
        elif key == K_2:
            return "leaderboard"