import pygame
import time
import random
import score
import data
import ai
import move
import collision
import background


pygame.init()

pygame.display.set_caption('Goblin gre v nebesa')

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)               
sky_blue = (172,225,255)


igraDisplay = pygame.display.set_mode((data.display_width,data.display_height))

ura = pygame.time.Clock()

game_score = score.Score()

background.generate_world()
background.load_world()
print(len(data.background_objects))

def draw(x, y, img):
    igraDisplay.blit(img, (x,y))


def text_objects(text, font):
    this_text = str(text)
    textSurface = font.render(this_text, True, red)  
    return textSurface, textSurface.get_rect()  

def message_display(text, size, opcija):
    largeText = pygame.font.SysFont('verdana', size)
    
    TextSurf, TextRect = text_objects(text, largeText)
    if opcija == 1:
        TextRect.center = ((data.display_width/2), (data.display_height/2 + 40))
    else:
        TextRect.center = ((data.display_width/2), (data.display_height/2))
    igraDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

def score_display(score):
    largeText = pygame.font.SysFont('verdana', 30)

    TextSurf, TextRect = text_objects(score, largeText)
    TextRect.center = (50,50)
    igraDisplay.blit(TextSurf, TextRect)
    

def crash():
    message_display('CRASHED!', 144, 0)  
    score_display(game_score.score)
    pygame.display.update()
    time.sleep(2)

    game_score.score = 0

    for enemy in data.list_of_chars:
        enemy.respawn()
    data.goblin.respawn()
    data.is_crashed = False
    
    
    game_loop()


message_display('Goblin gre v nebo PC igra', 24, 0)  
time.sleep(2)
message_display('2015', 30, 1)
time.sleep(5)


def game_loop():

    start_time = time.time()  
    
    gameExit = False

    while not gameExit:

        data.since_last_frame = ura.tick(60) / 1000.0

        ###########################DEBUGGING###########################
        #print(data.since_last_frame)
        #print(ura.get_fps())
        #print(data.goblin.x_speed * data.since_last_frame)
        ###############################################################

        move.scan_input() 
        ai.calc_enemies() 

        move.move_goblin()
        move.move_enemies() 

        collision.update_coll()
        collision.update_goblin_coll()

        collision.check_coll()

        igraDisplay.fill(sky_blue)

        if data.is_flying == True:
            moved = background.move_background()

            for obj in moved:
                draw(obj.x, obj.y, obj.img)

        else:
            objects = data.background_objects[0:20]
            objects.reverse()
            
            for obj in objects:
                draw(obj.x, obj.y, obj.img)

        draw(data.goblin.x, data.goblin.y, data.goblin.img)

        for obj in data.list_of_chars:
            draw(obj.x, obj.y, obj.img)
        
        ###########################################################DEBUGGING##################################
        #pygame.draw.rect(igraDisplay, red, [data.goblin_box[0].x, data.goblin_box[0].y, data.goblin_box[0].width, data.goblin_box[0].height])
        #pygame.draw.rect(igraDisplay, red, [data.goblin_box[1].x, data.goblin_box[1].y, data.goblin_box[1].width, data.goblin_box[1].height])
        #pygame.draw.rect(igraDisplay, red, [data.goblin_box[2].x, data.goblin_box[2].y, data.goblin_box[2].width, data.goblin_box[2].height])
        #pygame.draw.rect(igraDisplay, red, [data.goblin_box[3].x, data.goblin_box[3].y, data.goblin_box[3].width, data.goblin_box[3].height])
        #pygame.draw.rect(igraDisplay, red, [data.goblin_box[4].x, data.goblin_box[4].y, data.goblin_box[4].width, data.goblin_box[4].height])
        ##########################################################################################################
        score_display(game_score.get_score(start_time))

        pygame.display.update()

        if data.is_crashed == True:
            crash()




game_loop()
pygame.quit()
quit()