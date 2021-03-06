import pygame
from DynaBlaster import *
import time
import random
from definitions import *
from multiprocessing import Process, Pipe

pygame.init()

def button(text, x, y, width, height, inactive_color, active_color, action=None):
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + width > cur[0] > x and y + height > cur[1] > y:
        pygame.draw.rect(gameDisplay, active_color, (x, y, width, height))
        if click[0] == 1 and action != None:
            if action == "quit":
                pygame.quit()
                quit()

            if action == "multiplay":
                game_loop(2)

            if action == "play":
                game_loop(1)

    else:
        pygame.draw.rect(gameDisplay, inactive_color, (x, y, width, height))

    text_to_button(text, black, x, y, width, height)

def game_intro():
    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    intro = False
                elif event.key == pygame.K_q:

                    pygame.quit()
                    quit()

        gameDisplay.fill(white)
        message_to_screen("Welcome to Dyna Blaster!", green, -200, size="medium")
        message_to_screen("The objective is to destroy enemies with bomb", black, -30)
        message_to_screen("before they destroy you.", black, 10)
        message_to_screen("The more enemies you destroy, the harder they get.", black, 50)
        # message_to_screen("Press C to play, P to pause or Q to quit",black,180)

        button("play", 150, 400, 100, 50, green, light_green, action="play")
        button("multiplay", 350, 400, 100, 50, yellow, light_yellow, action="multiplay")
        button("quit", 550, 400, 100, 50, red, light_red, action="quit")

        pygame.display.update()

        clock.tick(15)

def main():
     play_game = Process(target = game_intro())
     play_game.daemon = True
     play_game.start()

if __name__ == '__main__':
     main()



