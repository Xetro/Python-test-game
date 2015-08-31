
import data

class Collision:
	
	def __init__(self, x, y, width, height):


		self.width = width
		self.height = height
		self.x = x
		self.y = y

		


def goblin_coll(x, y):
	# ustvari custom collision boxe za goblina
	print('Ustvari goblin boxe')
		
	box_1 = Collision(x + 34.0, y, 49.0, 49.0)
	box_2 = Collision(x + 32.0, y + 49.0, 52.0, 73.0)
	box_3 = Collision(x, y + 138.0, 78.0, 24.0)
	box_4 = Collision(x + 83.0, y + 16.0, 14.0, 11.0)
	box_5 = Collision(x + 84.0, y + 64.0, 52.0, 15.0)

	data.goblin_box.clear()
	data.goblin_box.extend((box_1, box_2, box_3, box_4, box_5))


def check_coll():
	for g_box in data.goblin_box:
		for box in data.list_of_boxes:
			##################################DEBUGGING##################################
			#print('g_box x:     %s  g_box y:       %s' % (g_box.x, g_box.y))
			#print('g_box width: %s  g_box height:  %s' % (g_box.width, g_box.height))
			#print('box x:       %s  box y:         %s' % (box.x, box.y))
			#print('box width:   %s  box height:    %s' % (box.width, box.height))
			#print('-----------------------------------------')
			############################################################################
			if box.x + box.width >= g_box.x + data.goblin.x_speed * data.since_last_frame and box.x <= g_box.x + data.goblin.x_speed * data.since_last_frame + g_box.width:
				if box.y + box.height >= g_box.y + data.goblin.y_speed * data.since_last_frame and box.y <= g_box.y + g_box.height + data.goblin.y_speed * data.since_last_frame: 
					data.is_crashed = True
					print('collTrue')
 

def update_coll():
	for i in range(0, len(data.list_of_chars)):	
		data.list_of_boxes[i].x = data.list_of_chars[i].x
		data.list_of_boxes[i].y = data.list_of_chars[i].y

def update_goblin_coll():
	x_speed = data.goblin.x_speed * data.since_last_frame
	y_speed = data.goblin.y_speed * data.since_last_frame

	data.goblin_box[0].x += x_speed
	data.goblin_box[1].x += x_speed
	data.goblin_box[2].x += x_speed
	data.goblin_box[3].x += x_speed
	data.goblin_box[4].x += x_speed

	data.goblin_box[0].y += y_speed
	data.goblin_box[1].y += y_speed
	data.goblin_box[2].y += y_speed
	data.goblin_box[3].y += y_speed
	data.goblin_box[4].y += y_speed



