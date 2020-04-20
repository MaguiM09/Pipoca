import math
import random
import pygame
from animal import Animal
from sprite_strip_anim import SpriteStripAnim
import constants

class Cat(Animal):
    """ This class represents an Animal. """
    # -- Methods
    def __init__(self):
        super().__init__()
        self.position.x = random.randint(0,constants.display_width)
        self.position.y = random.randint(0,constants.display_height)
        self.flock_distance = 5
        self.health = 100
        self.alone = False

    def follow(self, cats):
        """ check distances between other cats """
        cat_leader_x = cats[0].position.x
        cat_leader_y = cats[0].position.y
        dist_x = cat_leader_x - self.position.x
        dist_y = cat_leader_y - self.position.y
        dist = math.sqrt(dist_x**2 + dist_y**2)
        if self.position.x != cat_leader_x:
            if self.position.x > cat_leader_x:
                self.velocity.x *= -1 # *(abs(dist_x)/dist)
            elif self.position.x < cat_leader_x:
                self.velocity.x *= 1 # *(abs(dist_x)/dist)
            else:
                self.velocity.x = 0
        if self.position.y != cat_leader_y:
            if self.position.y > cat_leader_y:
                self.velocity.y *= -1 # *(abs(dist_y)/dist)
            elif self.position.y < cat_leader_y:
                self.velocity.y *= 1 # *(abs(dist_y)/dist)
            else:
                self.velocity.y = 0

    def flock(self, cats):
        """ check distances between other cats """
        # calculate distance between
        alone = True
        for cat in cats:
            dist_x =  self.position.x - cat.position.x
            dist_y =  cat.position.y - self.position.y
            dist = math.sqrt(dist_x**2 + dist_y**2)
            # print(dist)
            if dist != 0:
                if 1 <= dist <= self.flock_distance*2:
                    self.alone = False
                    # print("flock")
                    self.velocity -= cat.velocity

                    self.position.x += 1/dist_x
                    self.position.y += 1/dist_y

                    # self.velocity.x = 0
                    # self.velocity.y = 0