# animal class
import pygame
import constants
import random
#random.seed(3127)
import spritesheet
from sprite_strip_anim import SpriteStripAnim
from animal import Animal

class Dog(Animal):
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
        self.x = constants.display_width / 2 
        self.y = constants.display_height / 2 
        # Bottom constants.display_height - self.height

        ## Set speed vector of animal
        self.change_x = 0
        self.change_y = 0

        ## Initial direction right = 0 up = 1 left = 2 down = 3 
        self.direction = 0

        #self.strips = all_strips[random.randint(0,3)]

    def brownian_movement(self):
        # Calculate new brownian motion
        brown_change_x = (random.random()/2 - random.random()/2)/10
        brown_change_y = (random.random()/2 - random.random()/2)/10
        # Set speedchange vector of animal
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
        if abs(self.change_y) > (0.75)*abs(self.change_x):
            if self.change_y <= 0:
                self.direction = 1
            else:
                self.direction = 3            
        else:
            if self.change_x >= 0:
                self.direction = 0
            else:
                self.direction = 2
    def check_bounds(self):
        # Periodic boundary conditions
        if self.x > constants.display_width :
            self.x = 1
        elif self.x + self.width < 0:
            self.x = constants.display_width - self.width
        if self.y >= 1 + constants.display_height:
            self.y = 0
        elif self.y + self.height + 1 < 0:
            self.y = constants.display_height - self.height

    def update(self):
        """ Update change with brownian motion """
        self.brownian_movement()
        """ Move the player. """
        # Move left/right
        self.x += self.change_x
        # Move up/down
        self.y += self.change_y
        self.check_bounds()
        self.calculate_x_direction()



