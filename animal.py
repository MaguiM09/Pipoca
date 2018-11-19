# animal class
import pygame
import constants
import random
#random.seed(3127)
from sprite_strip_anim import SpriteStripAnim

class Animal(pygame.sprite.Sprite):
    """ This class represents an Animal. """
    # -- Methods
    def __init__(self):
        """ Constructor function """
 
        # Call the parent's constructor
        super().__init__()
        # -- Attributes
        ## Set image width and height
        self.width = 32
        self.height = 32

        ## Set location of animal initially to center of screen
        self.x = constants.display_width // 2 
        self.y = constants.display_height - self.height

        ## Set speed vector of animal
        self.change_x = 0
        self.change_y = 0

        ## Initial direction right = 0 up = 1 left = 2 down = 3 
        self.direction = 0

    def brownian_movement(self):
        # Calculate new brownian motion
        brown_change_x = random.random() - random.random()
        brown_change_y = 0
        # Set speedchange vector of animal
        if self.change_x > 2:
            self.change_x -= brown_change_x * brown_change_x
        elif self.change_x < -2:
            self.change_x += brown_change_x * brown_change_x
        else:
            self.change_x += brown_change_x
        self.change_y += brown_change_y

    # Not yet re-implemented    
    def calc_grav(self):
        """ Calculate effect of gravity. only when jumping """
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += .35

    def calculate_x_direction(self):
        """ Calculate direction to face in x - dimenion """
        if self.change_x > 0:
            self.direction = 0
        elif self.change_y < 0:
            self.direction = 2
        else: 
            self.direction = 3
    
    def update(self):
        """ Update change with brownian motion """
        self.brownian_movement()
        """ Move the player. """
        # Move left/right
        self.x += self.change_x
        # Move up/down
        self.y += self.change_y



