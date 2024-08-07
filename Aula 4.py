import pgzrun
from pgzhelper import *
from random import randint

WIDTH = 800
HEIGHT = 600

Alien = Actor ("alien_1")
Alien.fps = 10
Alien.images = ["alien_1" , "alien_2.png"]
Alien.pos = (WIDTH/2, HEIGHT-132)

icon = Actor("icon")
icon.pos = randint()


def draw ():
    screen.blit("desert" , (0,-150))
    Alien.draw()

def update ():
    move_alien()
    pass
    #Alien.animate()

def move_alien():
    if keyboard.left:
        Alien.animate()
        Alien.x -= 2
        Alien.flip_x = True
    elif keyboard.right:
        Alien.animate()
        Alien.x += 2
        Alien.flip_x = False


music.play("grass_theme")
music.set_volume(0.5)

pgzrun.go()
