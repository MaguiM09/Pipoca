"""
Global constants
"""
# Screen dimensions
import pygame
import cat
# import sys
import random
from sprite_strip_anim import SpriteStripAnim

display_width = 800
display_height = 800
size = (display_width, display_height)

FPS = 30
frames = FPS // 12

# Colors
background = (213, 248, 255)
black = (0,0,0)
white = (255,255,255)
yellow = (255, 252, 149)
purple = (240, 196, 255)
gray = (175, 175, 175)
red_gray = (213, 186, 193)
off_white = (255, 255, 245)

num_cats = 24
cat_color = random.randint(0,3)
n = 0

max_force = 0.5
max_speed = 4
perception = 100