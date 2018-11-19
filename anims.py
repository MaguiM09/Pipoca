import sys
import pygame
from pygame.locals import Color, KEYUP, K_ESCAPE, K_RETURN, K_w, K_a, K_s, K_d
import spritesheet
from sprite_strip_anim import SpriteStripAnim
import constants

FPS = 60
frames = FPS // 12

frames = constants.frames
# Load sprites
###########
# Dogs
## White Dog
dog_white_strips = [
    SpriteStripAnim('dog.png', (0,0,32,32), 3, 1, True, frames), # Walk Right
    SpriteStripAnim('dog.png', (32,0,32,32), 1, 1, True, frames), # Stand lool Right
    SpriteStripAnim('dog.png', (0,32,32,32), 3, 1, True, frames), # Walk Up
    SpriteStripAnim('dog.png', (32,32,32,32), 1, 1, True, frames), # Stand Up
    SpriteStripAnim('dog.png', (0,64,32,32), 3, 1, True, frames), # Walk Down
    SpriteStripAnim('dog.png', (32,64,32,32), 1, 1, True, frames), # Stand Down
    SpriteStripAnim('dog.png', (96,128,32,32), 1, 1, True, frames), # Stand Down Lick
    SpriteStripAnim('dog.png', (0,128,32,32), 4, 1, True, frames), # Eat Down 
    SpriteStripAnim('dog.png', (0,96,32,32), 3, 1, True, frames), # Walk Left
    SpriteStripAnim('dog.png', (32,96,32,32), 1, 1, True, frames), # Stand Left
    SpriteStripAnim('dog.png', (96,64,32,32), 1, 1, True, frames), # Standv2 Left
    SpriteStripAnim('dog.png', (96,96,32,32), 1, 1, True, frames), # Rest Left
    SpriteStripAnim('dog.png', (96,0,32,32), 1, 1, True, frames), # Rest Right
]
## Yellow Dog
dog_yellow_strips = [
    SpriteStripAnim('dog.png', (128+0,0,32,32), 3, 1, True, frames), # Walk Right
    SpriteStripAnim('dog.png', (128+32,0,32,32), 1, 1, True, frames), # Stand lool Right
    SpriteStripAnim('dog.png', (128+0,32,32,32), 3, 1, True, frames), # Walk Up
    SpriteStripAnim('dog.png', (128+32,32,32,32), 1, 1, True, frames), # Stand Up
    SpriteStripAnim('dog.png', (128+0,64,32,32), 3, 1, True, frames), # Walk Down
    SpriteStripAnim('dog.png', (128+32,64,32,32), 1, 1, True, frames), # Stand Down
    SpriteStripAnim('dog.png', (128+96,128,32,32), 1, 1, True, frames), # Stand Down Lick
    SpriteStripAnim('dog.png', (128+0,128,32,32), 4, 1, True, frames), # Eat Down 
    SpriteStripAnim('dog.png', (128+0,96,32,32), 3, 1, True, frames), # Walk Left
    SpriteStripAnim('dog.png', (128+32,96,32,32), 1, 1, True, frames), # Stand Left
    SpriteStripAnim('dog.png', (128+96,64,32,32), 1, 1, True, frames), # Standv2 Left
    SpriteStripAnim('dog.png', (128+96,96,32,32), 1, 1, True, frames), # Rest Left
    SpriteStripAnim('dog.png', (128+96,0,32,32), 1, 1, True, frames), # Rest Right
]
## Orange Dog
dog_orange_strips = [
    SpriteStripAnim('dog.png', (256+0,0,32,32), 3, 1, True, frames), # Walk Right
    SpriteStripAnim('dog.png', (256+32,0,32,32), 1, 1, True, frames), # Stand lool Right
    SpriteStripAnim('dog.png', (256+0,32,32,32), 3, 1, True, frames), # Walk Up
    SpriteStripAnim('dog.png', (256+32,32,32,32), 1, 1, True, frames), # Stand Up
    SpriteStripAnim('dog.png', (256+0,64,32,32), 3, 1, True, frames), # Walk Down
    SpriteStripAnim('dog.png', (256+32,64,32,32), 1, 1, True, frames), # Stand Down
    SpriteStripAnim('dog.png', (256+96,128,32,32), 1, 1, True, frames), # Stand Down Lick
    SpriteStripAnim('dog.png', (256+0,128,32,32), 4, 1, True, frames), # Eat Down 
    SpriteStripAnim('dog.png', (256+0,96,32,32), 3, 1, True, frames), # Walk Left
    SpriteStripAnim('dog.png', (256+32,96,32,32), 1, 1, True, frames), # Stand Left
    SpriteStripAnim('dog.png', (256+96,64,32,32), 1, 1, True, frames), # Standv2 Left
    SpriteStripAnim('dog.png', (256+96,96,32,32), 1, 1, True, frames), # Rest Left
    SpriteStripAnim('dog.png', (256+96,0,32,32), 1, 1, True, frames), # Rest Right
]
## Black Dog
dog_black_strips = [
    SpriteStripAnim('dog.png', (384+0,0,32,32), 3, 1, True, frames), # Walk Right
    SpriteStripAnim('dog.png', (384+32,0,32,32), 1, 1, True, frames), # Stand lool Right
    SpriteStripAnim('dog.png', (384+0,32,32,32), 3, 1, True, frames), # Walk Up
    SpriteStripAnim('dog.png', (384+32,32,32,32), 1, 1, True, frames), # Stand Up
    SpriteStripAnim('dog.png', (384+0,64,32,32), 3, 1, True, frames), # Walk Down
    SpriteStripAnim('dog.png', (384+32,64,32,32), 1, 1, True, frames), # Stand Down
    SpriteStripAnim('dog.png', (384+96,128,32,32), 1, 1, True, frames), # Stand Down Lick
    SpriteStripAnim('dog.png', (384+0,128,32,32), 4, 1, True, frames), # Eat Down 
    SpriteStripAnim('dog.png', (384+0,96,32,32), 3, 1, True, frames), # Walk Left
    SpriteStripAnim('dog.png', (384+32,96,32,32), 1, 1, True, frames), # Stand Left
    SpriteStripAnim('dog.png', (384+96,64,32,32), 1, 1, True, frames), # Standv2 Left
    SpriteStripAnim('dog.png', (384+96,96,32,32), 1, 1, True, frames), # Rest Left
    SpriteStripAnim('dog.png', (384+96,0,32,32), 1, 1, True, frames), # Rest Right
]
############
# Cats
## White Cat
cat_white_strips = [
    SpriteStripAnim('cat.png', (0,0,32,32), 3, 1, True, frames), # Walk Right
    SpriteStripAnim('cat.png', (32,0,32,32), 1, 1, True, frames), # Stand lool Right
    SpriteStripAnim('cat.png', (0,32,32,32), 3, 1, True, frames), # Walk Up
    SpriteStripAnim('cat.png', (32,32,32,32), 1, 1, True, frames), # Stand Up
    SpriteStripAnim('cat.png', (0,64,32,32), 3, 1, True, frames), # Walk Down
    SpriteStripAnim('cat.png', (32,64,32,32), 1, 1, True, frames), # Stand Down
    SpriteStripAnim('cat.png', (96,128,32,32), 1, 1, True, frames), # Stand Down Lick
    SpriteStripAnim('cat.png', (0,128,32,32), 4, 1, True, frames), # Eat Down 
    SpriteStripAnim('cat.png', (0,96,32,32), 3, 1, True, frames), # Walk Left
    SpriteStripAnim('cat.png', (32,96,32,32), 1, 1, True, frames), # Stand Left
    SpriteStripAnim('cat.png', (96,96,32,32), 1, 1, True, frames), # Rest Left
    SpriteStripAnim('cat.png', (96,0,32,32), 1, 1, True, frames), # Rest Right
]
## Yellow cat
cat_yellow_strips = [
    SpriteStripAnim('cat.png', (128+0,0,32,32), 3, 1, True, frames), # Walk Right
    SpriteStripAnim('cat.png', (128+32,0,32,32), 1, 1, True, frames), # Stand lool Right
    SpriteStripAnim('cat.png', (128+0,32,32,32), 3, 1, True, frames), # Walk Up
    SpriteStripAnim('cat.png', (128+32,32,32,32), 1, 1, True, frames), # Stand Up
    SpriteStripAnim('cat.png', (128+0,64,32,32), 3, 1, True, frames), # Walk Down
    SpriteStripAnim('cat.png', (128+32,64,32,32), 1, 1, True, frames), # Stand Down
    SpriteStripAnim('cat.png', (128+96,128,32,32), 1, 1, True, frames), # Stand Down Lick
    SpriteStripAnim('cat.png', (128+0,128,32,32), 4, 1, True, frames), # Eat Down 
    SpriteStripAnim('cat.png', (128+0,96,32,32), 3, 1, True, frames), # Walk Left
    SpriteStripAnim('cat.png', (128+32,96,32,32), 1, 1, True, frames), # Stand Left
    SpriteStripAnim('cat.png', (128+96,96,32,32), 1, 1, True, frames), # Rest Left
    SpriteStripAnim('cat.png', (128+96,0,32,32), 1, 1, True, frames), # Rest Right
]
## Orange cat
cat_orange_strips = [
    SpriteStripAnim('cat.png', (256+0,0,32,32), 3, 1, True, frames), # Walk Right
    SpriteStripAnim('cat.png', (256+32,0,32,32), 1, 1, True, frames), # Stand lool Right
    SpriteStripAnim('cat.png', (256+0,32,32,32), 3, 1, True, frames), # Walk Up
    SpriteStripAnim('cat.png', (256+32,32,32,32), 1, 1, True, frames), # Stand Up
    SpriteStripAnim('cat.png', (256+0,64,32,32), 3, 1, True, frames), # Walk Down
    SpriteStripAnim('cat.png', (256+32,64,32,32), 1, 1, True, frames), # Stand Down
    SpriteStripAnim('cat.png', (256+96,128,32,32), 1, 1, True, frames), # Stand Down Lick
    SpriteStripAnim('cat.png', (256+0,128,32,32), 4, 1, True, frames), # Eat Down 
    SpriteStripAnim('cat.png', (256+0,96,32,32), 3, 1, True, frames), # Walk Left
    SpriteStripAnim('cat.png', (256+32,96,32,32), 1, 1, True, frames), # Stand Left
    SpriteStripAnim('cat.png', (256+96,96,32,32), 1, 1, True, frames), # Rest Left
    SpriteStripAnim('cat.png', (256+96,0,32,32), 1, 1, True, frames), # Rest Right
]
## Black cat
cat_black_strips = [
    SpriteStripAnim('cat.png', (384+0,0,32,32), 3, 1, True, frames), # Walk Right
    SpriteStripAnim('cat.png', (384+32,0,32,32), 1, 1, True, frames), # Stand lool Right
    SpriteStripAnim('cat.png', (384+0,32,32,32), 3, 1, True, frames), # Walk Up
    SpriteStripAnim('cat.png', (384+32,32,32,32), 1, 1, True, frames), # Stand Up
    SpriteStripAnim('cat.png', (384+0,64,32,32), 3, 1, True, frames), # Walk Down
    SpriteStripAnim('cat.png', (384+32,64,32,32), 1, 1, True, frames), # Stand Down
    SpriteStripAnim('cat.png', (384+96,128,32,32), 1, 1, True, frames), # Stand Down Lick
    SpriteStripAnim('cat.png', (384+0,128,32,32), 4, 1, True, frames), # Eat Down 
    SpriteStripAnim('cat.png', (384+0,96,32,32), 3, 1, True, frames), # Walk Left
    SpriteStripAnim('cat.png', (384+32,96,32,32), 1, 1, True, frames), # Stand Left
    SpriteStripAnim('cat.png', (384+96,96,32,32), 1, 1, True, frames), # Rest Left
    SpriteStripAnim('cat.png', (384+96,0,32,32), 1, 1, True, frames), # Rest Right
]