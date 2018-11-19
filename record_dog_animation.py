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
import sys, os
import pygame
from pygame.locals import *
# import spritesheet
from sprite_strip_anim import SpriteStripAnim
import constants
# import anims
from animal import Animal
from dog import Dog
# import pygame.camera

def showImage(x,y):
    surface.blit(image,(x,y))

pygame.init()
# pygame.camera.init()
# Ensure we have somewhere for the frames
try:
    os.makedirs("Snaps")
except OSError:
    pass

pygame.display.set_caption('Dog Sprite')
surface = pygame.display.set_mode((constants.display_width,constants.display_height))
FPS = constants.FPS
frames = constants.frames
x = constants.display_width // 2
y = constants.display_height // 2
# Load sprites
## White dog as default sprite
strips = [
    SpriteStripAnim('dog.png', (0,0,32,32), 3, 0, True, frames), # Walk Right
    SpriteStripAnim('dog.png', (32,0,32,32), 1, 0, True, frames), # Stand lool Right
    SpriteStripAnim('dog.png', (0,32,32,32), 3, 0, True, frames), # Walk Up
    SpriteStripAnim('dog.png', (32,32,32,32), 1, 0, True, frames), # Stand Up
    SpriteStripAnim('dog.png', (0,64,32,32), 3, 0, True, frames), # Walk Down
    SpriteStripAnim('dog.png', (32,64,32,32), 1, 0, True, frames), # Stand Down
    SpriteStripAnim('dog.png', (96,128,32,32), 1, 0, True, frames), # Stand Down Lick
    SpriteStripAnim('dog.png', (0,128,32,32), 4, 0, True, frames), # Eat Down 
    SpriteStripAnim('dog.png', (0,96,32,32), 3, 0, True, frames), # Walk Left
    SpriteStripAnim('dog.png', (32,96,32,32), 1, 0, True, frames), # Stand Left
    SpriteStripAnim('dog.png', (96,96,32,32), 1, 0, True, frames), # Rest Left
    SpriteStripAnim('dog.png', (96,0,32,32), 1, 0, True, frames), # Rest Right
]

# black = Color('black')
clock = pygame.time.Clock()
# Create Initial Dogs
dogs = []
for i in range(64):
    dogs.append(Dog())
# Set up Continuous Loop
n = 0
strips[n].iter()
image = strips[n].next()

# cam = pygame.camera.Camera("/dev/video0", (constants.display_width, constants.display_height))
# cam.start()

file_num = 0
# done_capturing = False

while True:
    file_num = file_num + 1
    # image = cam.get_image()

    # Draw the background
    surface.fill(constants.background) 
    for dog in dogs:
        dog.update()
        if dog.direction == 0:
            n = 0
        elif dog.direction == 1:
            n = 2
        elif dog.direction == 2:
            n = 8
        elif dog.direction == 3:
            n = 4
        last_image = image
        image = strips[n].next()
        # Draw all dogs to the screen
        showImage(dog.x,dog.y)
        image = last_image

    # Save every frame
    filename = "Snaps/%04d.png" % file_num
    pygame.image.save(surface, filename)

    # Process Events
    for e in pygame.event.get():
        if e.type == KEYUP: # On User Key Press Up
            if e.key == K_ESCAPE:# End Game
                sys.exit()
            elif e.key == K_RETURN: # Toggle next strip
                n += 1
                if n >= len(strips):
                    n = 0
                strips[n].iter() # Go to next strip


    # for dog in dogs:
    pygame.display.flip()
    clock.tick(FPS)

# Combine frames to make video
os.system("ffmpeg -r 30 -f image2 -i Snaps/%04d.png result.avi")