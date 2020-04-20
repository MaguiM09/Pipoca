# animal class
import pygame
import constants
import random
#random.seed(3127)

from p5 import Vector, stroke, circle
import numpy as np

class Animal(pygame.sprite.Sprite):
    """ This class represents an Animal. """
    # -- Methods
    def __init__(self):
        """ Constructor function """
        self.random_start_x = random.randint(0,constants.display_width)
        self.random_start_y = random.randint(0,constants.display_height)
        # self.y = random.randint(0,constants.display_height)
        self.position = Vector(self.random_start_x, self.random_start_y)
        vec = (np.random.rand(2) - 0.5)*10
        self.velocity = Vector(*vec)
        self.last_position = self.position
        vec = (np.random.rand(2) - 0.5)/2
        self.acceleration = Vector(*vec)
        self.max_force = constants.max_force
        self.max_speed = constants.max_speed
        self.perception = constants.perception
        # self.width = constants.display_width
        # self.height = constants.display_height

        # Call the parent's constructor
        super().__init__()
        # -- Attributes
        ## Set image width and height
        self.width = 32
        self.height = 32

        ## Set location of animal initially to center of screen
        # self.position.x = constants.display_width / 2
        # self.position.y = constants.display_height / 2
        # Bottom constants.display_height - self.height

        ## Set speed vector of animal
        self.velocity.x = 0
        self.velocity.y = 0

        ## Initial direction right = 0 up = 1 left = 2 down = 3
        self.direction = 0
        self.max_health = 100
        self.health = self.max_health
        self.dead = False

    def check_health(self):
        if self.health <= 0:
            self.dead = True
        else:
            self.dead = False

    def brownian_movement(self):
        # Calculate new brownian motion
        brown_change_x = (random.random()/2 - random.random()/2)/10
        brown_change_y = (random.random()/2 - random.random()/2)/10
        # Set speedchange vector of animal
        if self.velocity.x > 2:
            self.velocity.x -= brown_change_x #* brown_change_x
        elif self.velocity.x < -2:
            self.velocity.x += brown_change_x #* brown_change_x
        else:
            self.velocity.x += brown_change_x
        self.velocity.y += brown_change_y

    # Not yet re-implemented
    def calc_grav(self):
        """ Calculate effect of gravity. only when jumping """
        if self.velocity.y == 0:
            self.velocity.y = 1
        else:
            self.velocity.y += .35

    def calculate_x_direction(self):
        """ Calculate direction to face in x - dimension """
        if self.last_position != self.position:
            if abs(self.velocity.y) > (0.8)*abs(self.velocity.x):
                if abs(self.velocity.y) > 0.2:
                    if self.velocity.y <= 0:
                        self.direction = 1
                    else:
                        self.direction = 3
            elif abs(self.velocity.y) < (0.7)*abs(self.velocity.x):
                if abs(self.velocity.x) > 0.2:
                    if self.velocity.x >= 0:
                        self.direction = 0
                    else:
                        self.direction = 2
            else:
                pass

    def check_bounds(self):
        # Periodic boundary conditions
        if self.position.x >= constants.display_width :
            self.position.x = 1
        elif self.position.x + self.width <= 0:
            self.position.x = constants.display_width - self.width
        if self.position.y >= 1 + constants.display_height:
            self.position.y = 0
        elif self.position.y + self.height + 1 <= 0:
            self.position.y = constants.display_height - self.height
            
    def check_collision(self, animal):
        # check if animals are colliding
        if (self.position.x, self.position.y) != (animal.position.x, animal.position.y):
            future_position_x = self.position.x + self.velocity.x
            future_position_y = self.position.y + self.velocity.y
            if animal.position.x - self.width <= future_position_x <= animal.position.x + animal.width:
                if animal.position.y + self.height >= future_position_y >= animal.position.y - animal.height:
                    # print("[INFO]: collision detected!")
                    self.velocity.x *= -1
                    self.velocity.y *= -1
                    self.acceleration.x *= -1
                    self.acceleration.y *= -1
                    # self.position.x += self.position.x - future_position_x
                    # self.position.x += self.position.x - future_position_x
                    self.health -= 1
                    self.brownian_movement()
                    # self.acceleration.x = 0
                    # self.acceleration.y = 0

    def update(self, animals=None):
        """ Update change with brownian motion """
        self.last_position = self.position
        if not self.dead:
        #     self.brownian_movement()
            if animals != None:
                for animal in animals:
                    if not animal.dead:
                        self.check_collision(animal)

            self.position += self.velocity
            self.velocity += self.acceleration
            self.calculate_x_direction()
            #limit
            if np.linalg.norm(self.velocity) > self.max_speed:
                self.velocity = self.velocity / np.linalg.norm(self.velocity) * self.max_speed

            self.acceleration = Vector(*np.zeros(2))
            self.check_bounds()


    def align(self, boids):
        steering = Vector(*np.zeros(2))
        total = 0
        avg_vector = Vector(*np.zeros(2))
        for boid in boids:
            if boid.dead == False:
                if np.linalg.norm(boid.position - self.position) < self.perception:
                    avg_vector += boid.velocity
                    total += 1
        if total > 0:
            avg_vector /= total
            avg_vector = Vector(*avg_vector)
            avg_vector = (avg_vector / np.linalg.norm(avg_vector)) * self.max_speed
            steering = avg_vector - self.velocity

        return steering

    def cohesion(self, boids):
        steering = Vector(*np.zeros(2))
        total = 0
        center_of_mass = Vector(*np.zeros(2))
        for boid in boids:
            if boid.dead == False:
                if np.linalg.norm(boid.position - self.position) < self.perception:
                    center_of_mass += boid.position
                    total += 1
        if total > 0:
            center_of_mass /= total
            center_of_mass = Vector(*center_of_mass)
            vec_to_com = center_of_mass - self.position
            if np.linalg.norm(vec_to_com) > 0:
                vec_to_com = (vec_to_com / np.linalg.norm(vec_to_com)) * self.max_speed
            steering = vec_to_com - self.velocity
            if np.linalg.norm(steering)> self.max_force:
                steering = (steering /np.linalg.norm(steering)) * self.max_force

        return steering

    def separation(self, boids):
        steering = Vector(*np.zeros(2))
        total = 0
        avg_vector = Vector(*np.zeros(2))
        for boid in boids:
            if boid.dead == False:
                distance = np.linalg.norm(boid.position - self.position)
                if self.position != boid.position and distance < self.perception and distance != 0:
                    diff = self.position - boid.position
                    diff /= distance
                    avg_vector += diff
                    total += 1
        if total > 0:
            avg_vector /= total
            avg_vector = Vector(*avg_vector)
            if np.linalg.norm(steering) > 0:
                avg_vector = (avg_vector / np.linalg.norm(steering)) * self.max_speed
            steering = avg_vector - self.velocity
            if np.linalg.norm(steering) > self.max_force:
                steering = (steering /np.linalg.norm(steering)) *3 *self.max_force

        return steering
    
    def apply_behavior(self, boids):
        alignment = self.align(boids)
        cohesion = self.cohesion(boids)
        separation = self.separation(boids)

        self.acceleration += alignment
        self.acceleration += cohesion
        self.acceleration += separation


    def reset(self):
        """ Set back to original position """
        self.dead = False
        self.health = self.max_health
        self.position.x = self.random_start_x
        self.position.y = self.random_start_y
        self.velocity.x = 0
        self.velocity.y = 0

    def respawn(self):
        """ respawn """
        self.dead = False
        self.health = self.max_health
        """ Set back to original position """
        self.position.x = self.random_start_x
        self.position.y = self.random_start_y
        self.velocity.x = 0
        self.velocity.y = 0