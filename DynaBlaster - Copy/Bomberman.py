import pygame
import os
from definitions import *
import time

iconSize =40
sirina = 19
visina = 13

class Bomberman(pygame.sprite.Sprite):
    def __init__(self, img, case1, case2): #prosledjujemo slicicu i pocetnu poziciju igraca
        self.image = pygame.image.load(os.path.join('Slike',img)).convert()
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()

        self.total_score = 0
        self.enemy_points = 10
        self.wall_points = 2
        self.total_lives = 3
        # score
        self.score_cfg = pygame.font.SysFont('Helvetica', 20, True)
        self.health_cfg = pygame.font.SysFont('Helvetica', 20, True)

        self.case_x = case1
        self.case_y = case2
        self.x = iconSize * self.case_x
        self.y = iconSize * self.case_y

        self.hidden = False
        self.hide_timer = pygame.time.get_ticks()

    def move(self, direction, enemy_list, world):
        if direction == "r":
            if self.case_x < (sirina - 1):
                if wallsPositions[self.case_x+1][self.case_y] == 0 or wallsPositions[self.case_x+1][self.case_y] == -1:
                    self.case_x += 1
                    self.x = self.case_x * iconSize

        if direction == "l":
            if self.case_x > 0:
                if wallsPositions[self.case_x-1][self.case_y] == 0 or wallsPositions[self.case_x-1][self.case_y] == -1:
                    self.case_x -= 1
                    self.x = self.case_x * iconSize

        if direction == "d":
            #if self.case_y > 0:
                if wallsPositions[self.case_x][self.case_y+1] == 0 or wallsPositions[self.case_x][self.case_y+1] == -1:
                    self.case_y += 1
                    self.y = self.case_y * iconSize

        if direction == "u":
            #if self.case_y < (visina - 1):
                if wallsPositions[self.case_x][self.case_y-1] == 0 or wallsPositions[self.case_x][self.case_y-1] == -1:
                    self.case_y -= 1
                    self.y = self.case_y * iconSize



 # score se uvecava kad ubije nekog
    def score_up(self, points_type):
        if points_type == 1: # prosledjujemo 1 kad ubijemo neprijatelja
            self.total_score += self.enemy_points
        elif points_type == 2: # prosledjujemo 1 kad unistimo zid
            self.total_score += self.wall_points

    # prikaz score
    def show_score(self, world, no):  #no je redni broj igraca
        if no == 1:
            self.score = self.score_cfg.render('Score1: ' + str(self.total_score), True, (255, 230, 0))
            world.blit(self.score, (10, 10))
        else:
            self.score = self.score_cfg.render('Score2: ' + str(self.total_score), True, (255, 230, 0))
            world.blit(self.score, (580, 10))

    def hide(self):
        self.hidden = True
        self.hide_timer = pygame.time.get_ticks()
        self.x = worldy   #privremeno ga sklanjamo sa ekrana
        self.y = worldy + 80

    def update(self, no):
        if self.hidden and pygame.time.get_ticks() - self.hide_timer > 3000:
            self.hidden = False

            if no == 1:
                #vrati ga na pocetak
                self.x = iconSize
                self.y = iconSize
            else:
                self.x = 17*iconSize
                self.y = 11*iconSize


    # smanjenje zivota
    def lives_down(self, world, no):
        self.total_lives -= 1
        # if self.total_lives == 0:
        #     pygame.quit()

        self.hide()

        # if no == 1:
        #     #vrati ga na pocetak
        #     self.x = iconSize
        #     self.y = iconSize
        # else:
        #     self.x = 17*iconSize
        #     self.y = 11*iconSize

    def lives_up(self, world, no):
        self.total_lives += 1
    # prikaz zivota
    def show_lives(self, world, no):
        if no == 1:
            self.health = self.health_cfg.render('Lives1: ' + str(self.total_lives), True, (255, 230, 0))
            world.blit(self.health, (120, 10))
        else:
            self.health = self.health_cfg.render('Lives2: ' + str(self.total_lives), True, (255, 230, 0))
            world.blit(self.health, (690, 10))
