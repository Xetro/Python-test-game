import pygame
import data
import collision


def scan_input():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if data.has_jumped == False:
                    data.goblin.y_speed = data.jump_speed


            if event.key == pygame.K_LEFT:
                if data.right_is_prsd == True:
                    data.goblin.stop()
                else:
                    data.goblin.move_left()
                
                data.left_is_prsd = True 
            
            elif event.key == pygame.K_RIGHT:
                if data.left_is_prsd == True:
                    data.goblin.stop()
                else:
                    data.goblin.move_right()

                data.right_is_prsd = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                if data.right_is_prsd == True:
                    data.goblin.move_right()
                else:
                    data.goblin.stop()

                data.left_is_prsd = False


            elif event.key == pygame.K_RIGHT:
                if data.left_is_prsd == True:
                    data.goblin.move_left()
                else:
                    data.goblin.stop()

                data.right_is_prsd = False

def move_enemies():
    for enemy in data.list_of_chars:
        enemy.x += enemy.x_speed * data.since_last_frame
        enemy.y += enemy.y_speed * data.since_last_frame



def move_goblin():

    if data.goblin.x + (data.goblin.x_speed * data.since_last_frame) < 0 or data.goblin.x + (data.goblin.x_speed * data.since_last_frame) + data.goblin.width > data.display_width:
        data.goblin.x_speed = 0

    if data.goblin.y <= 250:
        data.goblin.y_speed = 0
        data.is_flying = True


    data.goblin.x += data.goblin.x_speed * data.since_last_frame
    data.goblin.y += data.goblin.y_speed * data.since_last_frame
