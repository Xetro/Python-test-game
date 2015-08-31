import pygame
import data
import random

cloud_1_img = pygame.image.load('cloud_1.png')
cloud_2_img = pygame.image.load('cloud_2.png')
cloud_3_img = pygame.image.load('cloud_3.png')
cloud_4_img = pygame.image.load('cloud_4.png')
cloud_5_img = pygame.image.load('cloud_5.png')
dirt_img = pygame.image.load('dirt.png')

tile_size = 50
row_num = (data.display_height * 50) / tile_size
col_num = data.display_width / tile_size
tile_map = []


class Background:
	def __init__(self, x, y, img):
		self.x = x
		self.y = y
		self.img = img

def generate_world():
	
	space_avalible = True	
	a = 0
	while a < (row_num):
		row = []
		b = 0
		
		while b < (col_num):
			space_avalible = check_space(a, b, row)
			spawn_obj = random.randrange(1, 60)

			if a == 0 and b == 0:
				row.append(1)
				
			elif spawn_obj == 1 and a > 4 and space_avalible == True:
				
				row.append(random.randrange(2, 7))

			else:		
				row.append(0)

			b += 1
			
		tile_map.append(row)

		a += 1
		
def check_space(a, b, row):
	tiles = []
	if a > 4:
		if b >= 5:
			tiles.append(row[b-5:b])

		elif b != 0:
			tiles.append(row[0:b])

		for i in range(1,5):
			tiles.append(tile_map[a-i][b:b+5])

			if b < 5:
				tiles.append(tile_map[a-i][0:b])

			else:
				tiles.append(tile_map[a-i][b-5:b])

		for tile in tiles:
			if ( 2 in tile ) or ( 3 in tile ) or ( 4 in tile ) or ( 5 in tile ) or ( 6 in tile ):
				return False


		else: 
			return True

	else:
		return False

def load_world():
	for i in range(0, int(row_num)):
		for c, a in enumerate(tile_map[i]):
			
			if a == 1:
				obj = Background(0, 550, dirt_img)
				data.background_objects.append(obj)

			if a == 2:
				obj = Background(c * tile_size - 500, data.display_height - (i * tile_size), cloud_1_img)
				data.background_objects.append(obj)

			if a == 3:
				obj = Background(c * tile_size -500, data.display_height - (i * tile_size), cloud_2_img)
				data.background_objects.append(obj)

			if a == 4:
				obj = Background(c * tile_size, data.display_height - (i * tile_size), cloud_3_img)
				data.background_objects.append(obj)

			if a == 5:
				obj = Background(c * tile_size - 500, data.display_height - (i * tile_size), cloud_4_img)
				data.background_objects.append(obj)

			if a == 6:
				obj = Background(c * tile_size - 500, data.display_width - (i * tile_size), cloud_5_img)
				data.background_objects.append(obj)

def move_background():

	moved_objects = []
	cntr = 0
	for obj in data.background_objects[0:20]:
		obj.y += 120 * data.since_last_frame
		if obj.y > data.display_height:
			data.background_objects.remove(obj)
			data.background_objects[20 + cntr].y += data.altitude
			cntr += 1
		else:
			moved_objects.append(obj)

	data.altitude += 120 * data.since_last_frame	
	return moved_objects






















