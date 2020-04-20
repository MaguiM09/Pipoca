"""
Sprite strip dog and cat animator
sample sprite strip is from bluecarrot16
http://opengameart.org/content/lpc-cats-and-dogs
Requires spritesheet.spritesheet and the
Copyright/Attribution Notice:
"[LPC] Cats and Dogs"
 Artist: bluecarrot16
 License: CC-BY 3.0 / GPL 3.0 / GPL 2.0 / OGA-BY 3.0

"""
import sys
import pygame
from pygame.locals import Color, K_q, KEYUP, K_ESCAPE, K_RETURN, K_w, K_a, K_s, K_d
from sprite_strip_anim import SpriteStripAnim
import constants
from animal import Animal
import cat
#import text_input
import os
import utils
import numpy as np
game = utils.Game()
game.cats = []
for i in range(constants.num_cats):
    game.cats.append(cat.Cat())

bg_color = constants.background

pygame.display.set_caption('Cats!')
pygame.display.init()
clock = pygame.time.Clock()

# textinput = text_input.TextInput()

total_strips = [[
    SpriteStripAnim('cat.png', (256+0,0,32,32), 3, 0, True, constants.frames), # Walk Right
    SpriteStripAnim('cat.png', (256+32,0,32,32), 1, 0, True, constants.frames), # Stand lool Right
    SpriteStripAnim('cat.png', (256+0,32,32,32), 3, 0, True, constants.frames), # Walk Up
    SpriteStripAnim('cat.png', (256+32,32,32,32), 1, 0, True, constants.frames), # Stand Up
    SpriteStripAnim('cat.png', (256+0,64,32,32), 3, 0, True, constants.frames), # Walk Down
    SpriteStripAnim('cat.png', (256+32,64,32,32), 1, 0, True, constants.frames), # Stand Down
    SpriteStripAnim('cat.png', (256+96,128,32,32), 1, 0, True, constants.frames), # Stand Down Lick
    SpriteStripAnim('cat.png', (256+0,128,32,32), 4, 0, True, constants.frames), # Eat Down
    SpriteStripAnim('cat.png', (256+0,96,32,32), 3, 0, True, constants.frames), # Walk Left
    SpriteStripAnim('cat.png', (256+32,96,32,32), 1, 0, True, constants.frames), # Stand Left
    SpriteStripAnim('cat.png', (256+96,96,32,32), 1, 0, True, constants.frames), # Rest Left
    SpriteStripAnim('cat.png', (256+96,0,32,32), 1, 0, True, constants.frames), # Rest Right
], [
    SpriteStripAnim('cat.png', (128+0,0,32,32), 3, 0, True, constants.frames), # Walk Right
    SpriteStripAnim('cat.png', (128+32,0,32,32), 1, 0, True, constants.frames), # Stand lool Right
    SpriteStripAnim('cat.png', (128+0,32,32,32), 3, 0, True, constants.frames), # Walk Up
    SpriteStripAnim('cat.png', (128+32,32,32,32), 1, 0, True, constants.frames), # Stand Up
    SpriteStripAnim('cat.png', (128+0,64,32,32), 3, 0, True, constants.frames), # Walk Down
    SpriteStripAnim('cat.png', (128+32,64,32,32), 1, 0, True, constants.frames), # Stand Down
    SpriteStripAnim('cat.png', (128+96,128,32,32), 1, 0, True, constants.frames), # Stand Down Lick
    SpriteStripAnim('cat.png', (128+0,128,32,32), 4, 0, True, constants.frames), # Eat Down
    SpriteStripAnim('cat.png', (128+0,96,32,32), 3, 0, True, constants.frames), # Walk Left
    SpriteStripAnim('cat.png', (128+32,96,32,32), 1, 0, True, constants.frames), # Stand Left
    SpriteStripAnim('cat.png', (128+96,96,32,32), 1, 0, True, constants.frames), # Rest Left
    SpriteStripAnim('cat.png', (128+96,0,32,32), 1, 0, True, constants.frames), # Rest Right
], [
    SpriteStripAnim('cat.png', (384+0,0,32,32), 3, 0, True, constants.frames), # Walk Right
    SpriteStripAnim('cat.png', (384+32,0,32,32), 1, 0, True, constants.frames), # Stand lool Right
    SpriteStripAnim('cat.png', (384+0,32,32,32), 3, 0, True, constants.frames), # Walk Up
    SpriteStripAnim('cat.png', (384+32,32,32,32), 1, 0, True, constants.frames), # Stand Up
    SpriteStripAnim('cat.png', (384+0,64,32,32), 3, 0, True, constants.frames), # Walk Down
    SpriteStripAnim('cat.png', (384+32,64,32,32), 1, 0, True, constants.frames), # Stand Down
    SpriteStripAnim('cat.png', (384+96,128,32,32), 1, 0, True, constants.frames), # Stand Down Lick
    SpriteStripAnim('cat.png', (384+0,128,32,32), 4, 0, True, constants.frames), # Eat Down
    SpriteStripAnim('cat.png', (384+0,96,32,32), 3, 0, True, constants.frames), # Walk Left
    SpriteStripAnim('cat.png', (384+32,96,32,32), 1, 0, True, constants.frames), # Stand Left
    SpriteStripAnim('cat.png', (384+96,96,32,32), 1, 0, True, constants.frames), # Rest Left
    SpriteStripAnim('cat.png', (384+96,0,32,32), 1, 0, True, constants.frames), # Rest Right
], [
    SpriteStripAnim('cat.png', (0,0,32,32), 3, 0, True, constants.frames), # Walk Right
    SpriteStripAnim('cat.png', (32,0,32,32), 1, 0, True, constants.frames), # Stand lool Right
    SpriteStripAnim('cat.png', (0,32,32,32), 3, 0, True, constants.frames), # Walk Up
    SpriteStripAnim('cat.png', (32,32,32,32), 1, 0, True, constants.frames), # Stand Up
    SpriteStripAnim('cat.png', (0,64,32,32), 3, 0, True, constants.frames), # Walk Down
    SpriteStripAnim('cat.png', (32,64,32,32), 1, 0, True, constants.frames), # Stand Down
    SpriteStripAnim('cat.png', (96,128,32,32), 1, 0, True, constants.frames), # Stand Down Lick
    SpriteStripAnim('cat.png', (0,128,32,32), 4, 0, True, constants.frames), # Eat Down
    SpriteStripAnim('cat.png', (0,96,32,32), 3, 0, True, constants.frames), # Walk Left
    SpriteStripAnim('cat.png', (32,96,32,32), 1, 0, True, constants.frames), # Stand Left
    SpriteStripAnim('cat.png', (96,96,32,32), 1, 0, True, constants.frames), # Rest Left
    SpriteStripAnim('cat.png', (96,0,32,32), 1, 0, True, constants.frames), # Rest Right
]]



p = total_strips[constants.cat_color]
total_strips[constants.cat_color][constants.n].iter() # Go to next strip
image = total_strips[constants.cat_color][constants.n].next()

def set_bg_white(): # off-white
    game.bg_color = constants.off_white
    # return constants.off_white
def set_bg_yellow(): # yellow
    game.bg_color = constants.yellow
    # return constants.yellow
def set_bg_purple(): # purple
    game.bg_color = constants.purple
    # return constants.purple
def set_bg_red_gray(): # red_gray
    game.bg_color = constants.red_gray
    # return constants.red_gray

background = (213, 248, 255)
black = (0,0,0)
white = (255,255,255)
yellow = (255, 252, 149)
purple = (240, 196, 255)
gray = (175, 175, 175)
red_gray = (213, 186, 193)
off_white = (255, 255, 245)

while True:

    game.display.fill(game.bg_color)

    events = pygame.event.get()

    """ Disabled input text """
    # if textinput.update(events):
    #     input_text = textinput.get_text()
    #     # print(input_text)
    # game.display.blit(textinput.get_surface(), (10, 10))
    game.button(msg="reset",x=100,y=770,w=60,h=20,ic=constants.gray,ac=constants.white,action=game.reset)
    game.button_status(msg="apply",x=400,y=770,w=60,h=20,ic=constants.gray,ac=constants.white,action=game.toggle_behavior, status=game.applying_behavior)
    game.button_status(msg="follow",x=730,y=770,w=60,h=20,ic=constants.gray,ac=constants.white,action=game.toggle_following, status=game.is_following)
    game.button_status(msg="flock",x=670,y=770,w=50,h=20,ic=constants.gray,ac=constants.white,action=game.toggle_flocking, status=game.is_flocking)

    game.button(msg="", x=640,y=770,w=20,h=20,ic=constants.off_white,ac=constants.white,action=set_bg_white)
    game.button(msg="", x=610,y=770,w=20,h=20,ic=constants.yellow,ac=constants.white, action=set_bg_yellow)
    game.button(msg="", x=580,y=770,w=20,h=20,ic=constants.purple,ac=constants.white,action=set_bg_purple)
    game.button(msg="", x=550,y=770,w=20,h=20,ic=constants.red_gray,ac=constants.white,action=set_bg_red_gray)

    for i, cat in enumerate(game.cats):

        if cat.dead:
            cat.respawn()



        if game.is_flocking:
            cat.flock(game.cats)
        if game.is_following:
            cat.follow(game.cats)
        if game.applying_behavior:
            cat.apply_behavior(game.cats)

        if game.collisions:
            for j, kat in enumerate(game.cats):
                if j!=i: # if not this cat
                    cat.check_collision(kat)


        cat.check_health()

        if cat.direction == 0:
            constants.n = 0
        elif cat.direction == 1:
            constants.n = 2
        elif cat.direction == 2:
            constants.n = 8
        elif cat.direction == 3:
            constants.n = 4


        cat.update(game.cats)
        cat.check_bounds()
        # Draw all cats to the screen
        if not cat.dead:
            image = total_strips[constants.cat_color][constants.n].next()
            if not np.isnan(cat.position.x) and not np.isnan(cat.position.y):
                game.showImage(image, cat.position.x, cat.position.y)
                last_image = image
            else:
                cat.reset()
            # image = last_image

    # Process Events
    for e in events:
        if e.type == pygame.QUIT:
            exit()
        if e.type == KEYUP: # On User Key Press Up
            if e.key == K_RETURN: # Toggle next strip
                constants.n += 1
                if constants.n >= len(p):
                    constants.n = 0
            if e.key == K_q:
                exit()
    # pygame.display.update()
    # image = total_strips[constants.cat_color][constants.n].next()
    pygame.display.flip()
    clock.tick(constants.FPS)

