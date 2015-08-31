
import characters
import data


def calc_enemies():
	for enemy in data.list_of_chars:
		if enemy.char_type == 2:
			if enemy.y < data.display_height:
				enemy.move_down()
			else:
				enemy.respawn()

		elif enemy.char_type == 3:
			if enemy.x < data.display_width:
				enemy.move_right()
			else:
				enemy.respawn()