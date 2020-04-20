import pygame
import sys
from pygame.locals import Color, KEYUP, K_ESCAPE, K_RETURN, K_w, K_a, K_s, K_d
# from sprite_strip_anim import SpriteStripAnim
import constants
from animal import Animal
import cat
import text_input
import os

class Game:

    def __init__(self):
        self.display = pygame.display.set_mode((constants.display_width,constants.display_height))
        self.bg_color = (constants.background)
        self.collisions = True
        self.is_following = False
        self.is_flocking = False
        self.applying_behavior = False
        self.intro = False
        self.menu = True
        self.controls = False
        self.playing = False
        self.floor_height_factor = 0.64
        self.is_clicking = False # help with click control management
        self.inputs = {
            "up" : pygame.K_UP,
            "down" : pygame.K_DOWN,
            "left" : pygame.K_LEFT,
            "right" : pygame.K_RIGHT,
            "w" : pygame.K_w,
            "a" : pygame.K_a,
            "s" : pygame.K_s,
            "d" : pygame.K_d
        }
        self.cats = []

    def reset(self):
        for cat in self.cats:
            cat.position.x = cat.random_start_x
            cat.position.y = cat.random_start_y

    def toggle_flocking(self):
        if self.is_flocking:
            self.is_flocking = False
        else:
            self.is_flocking = True

    def toggle_following(self):
        if self.is_following:
            self.is_following = False
        else:
            self.is_following = True
        
    def toggle_behavior(self):
        if self.applying_behavior:
            self.applying_behavior = False
        else:
            self.applying_behavior = True
    
    def update_up(self):
        self.inputs["up"] = self.inputs["w"]

    def open_controls(self):
        self.menu = False
        self.controls = True

    def open_menu(self):
        self.menu = True
        self.controls = False
        self.playing = False

    def open_playing(self):
        self.menu = False
        self.playing = True

    def text_objects(self,text, font):
        textSurface = font.render(text, True, (1,155,179))
        return textSurface, textSurface.get_rect()

    def button(self, msg,x,y,w,h,ic,ac,action=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x+w > mouse[0] > x and y+h > mouse[1] > y:
            pygame.draw.rect(self.display, ac,(x,y,w,h))

            if not self.is_clicking and click[0] == 1 and action != None:
                self.is_clicking = True
                action()         
        else:
            pygame.draw.rect(self.display, ic,(x,y,w,h))
        # help with click control
        if click[0] == 0:
            self.is_clicking = False

        smallText = pygame.font.SysFont("dejavusansmono",30)
        textSurf, textRect = self.text_objects(msg, smallText)
        textRect.center = ( (x+(w/2)), (y+(h/2)) )
        self.display.blit(textSurf, textRect)

    def button_status(self, msg,x,y,w,h,ic,ac,action=None,status=None):
        """ status is a boolean representing the boolean i.e. game.is_following """
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        color_mod = 0.5
        if status != None:
            if status:
                ac = [int(ac[0]*color_mod), int(ac[1]*color_mod), int(ac[2]*color_mod)]
                ic = [int(ic[0]*color_mod), int(ic[1]*color_mod), int(ic[2]*color_mod)]

        if x+w > mouse[0] > x and y+h > mouse[1] > y:
            pygame.draw.rect(self.display, ac,(x,y,w,h))

            if not self.is_clicking and click[0] == 1 and action != None:
                self.is_clicking = True
                action()         
        else:
            pygame.draw.rect(self.display, ic,(x,y,w,h))
        # help with click control
        if click[0] == 0:
            self.is_clicking = False

        smallText = pygame.font.SysFont("dejavusansmono",30)
        textSurf, textRect = self.text_objects(msg, smallText)
        textRect.center = ( (x+(w/2)), (y+(h/2)) )
        self.display.blit(textSurf, textRect)

    def showImage(self, image, x, y):
        try:
            self.display.blit(image,(x,y))
        except:
            print("[INFO]: Failed to print to screen at {}, {}".format(x,y))


# def button_text(msg, x, y, w, h):
#     smallText = pygame.font.Font(wd + 'Quicksand-SemiBold.ttf',15)
#     textSurf, textRect = constants.text_objects(msg, smallText)
#     textRect.center = (x+(w/2), y+(h/2))
#     game.display.blit(textSurf, textRect)