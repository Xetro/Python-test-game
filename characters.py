import collision
import data
import random


class Character:
	
	x_speed = 0
	y_speed = 0

	char_type = 0 # 1 spawna na začetni lokaciji, 2 na zgornji strani random x, 3 na levi strani random y

	def __init__(self, x, y, width, height, base_speed, img, char_type):
		self.x = x		
		self.y = y
		self.start_x = x
		self.start_y = y
		self.width = width
		self.height = height
		self.img = img
		self.base_speed = base_speed
		self.char_type = char_type
		print("narejen karakter")
		if self.char_type != 1:
			data.list_of_chars.append(self)

			box = collision.Collision(x, y, width, height)
			data.list_of_boxes.append(box)
			print("Addan v char in box list")

		else:
			collision.goblin_coll(x, y)


	def move_left(self):
		self.x_speed = -self.base_speed
	
	def move_right(self):
		self.x_speed = self.base_speed

	def move_up(self):
		self.y_speed = -self.base_speed

	def move_down(self):
		self.y_speed = self.base_speed

	def stop(self):
		self.x_speed = 0

	def respawn(self):
		if self.char_type == 1:
			self.x = self.start_x
			self.y = self.start_y
			collision.goblin_coll(self.start_x, self.start_y)

		elif  self.char_type == 2:
			self.x = random.randrange(0, data.display_width - self.width)
			self.y = self.start_y

		elif self.char_type ==3:
			self.x = self.start_x
			self.y = random.randrange(0, data.display_height - self.height)