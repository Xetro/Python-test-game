import pygame
from characters import Character
import random

display_width = 800
display_height = 600

since_last_frame = 1.0

goblin_img = pygame.image.load('goblin.png')
thing_img = pygame.image.load('thing.png')


list_of_chars = []
list_of_boxes = []
goblin_box = []
background_objects = []

goblin_width  = 136
goblin_height = 162
goblin_speed = 360
jump_speed = -120
is_flying = False
altitude = 0
moved = 0

thing_width = 100
thing_height = 100
thing_speed = 140

start_x = display_width * 0.45
start_y = display_height * 0.7

thing_startx = random.randrange(0, display_width - thing_width)
thing_starty = -800

left_is_prsd = False
right_is_prsd = False
has_jumped = False

goblin = Character(start_x, start_y, goblin_width, goblin_height, goblin_speed, goblin_img, 1)
thing = Character(thing_startx, thing_starty, thing_width, thing_height, thing_speed, thing_img, 2)

is_crashed = False