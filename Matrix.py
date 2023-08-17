import pygame
import random
import math
from pygame.locals import *

pygame.init()

display_width = 1920 
display_height = 1080 
screen = pygame.display.set_mode((display_width, display_height))
clock = pygame.time.Clock()
screen.fill('Black')
font_name = 'Times New Roman'
font_size = 12
font = pygame.font.SysFont(font_name, font_size)
#height_buffer = input('Height Buffer:')
#space_buffer = input('Space Buffer:')
input_text = 'H'

text_width, text_height = font.size(input_text)
matrix_width = display_width//text_width
matrix_height = display_height//text_height

global CHOICES
CHOICES = '10'
INFLECTION_PT = (display_width//2, display_height//2)

Matrix = [[random.choice(CHOICES) for i in range(matrix_width)] for j in range(matrix_height)]
Matrix_Offsets = [[(0,0) for i in range(matrix_width)] for j in range (matrix_height)]


def regen_matrix():
    for y in range(matrix_height):
        for x in range(matrix_width):
           Matrix[y][x] = random.choice(CHOICES)
"""
def shk_wave_update(stoptime, inf_pt, tick_value):
    if stoptime == tick:
        global shockwave
        print('Shockwave Over')
        shockwave = False
        return
    else:
        for y in range (matrix_height):
            for x in range(matrix_width):
                dx = inf_pt[0] - x
                dy = inf_pt[1] - y
                distance = int(math.sqrt(dx ** 2 + dy ** 2))
                time = tick_value - stopping_time
                wave_offset = scale * math.exp(-((distance ** 2) / (2 * spread ** 2))) * math.cos(t * decay_factor)
                intensity_tuple = (int(wave_offset), int(wave_offset))
                Matrix_Offsets[y][x] = intensity_tuple
                #slope = dy // dx
                print(distance)
                #print(slope)
            #wave_offset_x = x + int((intensity * (scale - distance)))
            #wave_offset_y = y + int((intensity * (scale - distance)))
            #intensity_tuple = (wave_offset_x,wave_offset_y)
            #Matrix_Offsets[y][x] =  intensity_tuple
"""



global tick
tick = 0
global shockwave 
shockwave = False
scale = 20
spread = 2 
decayfactor = 0.05
duration = 20

while True:
    
    
    screen.fill('Black')
    INFLECTION_PT


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                pygame.quit()
                exit()
        if event.type == MOUSEBUTTONUP:
            INFLECTION_PT = pygame.mouse.get_pos()
            print(INFLECTION_PT)
            shockwave = True
            stopping_time = tick + duration
            print(stopping_time)

    #if shockwave == True:
    #    shk_wave_update(stopping_time,INFLECTION_PT,tick)



    for y in range(matrix_height):
        for x in range(matrix_width):
            letter = font.render(Matrix[y][x], True, (0,255,0))
            letter_x = x  * (text_width + text_width)
            letter_y = y * (text_height) 
            pos_x = letter_x + Matrix_Offsets[y][x][0]
            pos_y = letter_y + Matrix_Offsets[y][x][1]
            #wave_function()
            screen.blit(letter, (pos_x, pos_y))
    
    
    
    tick += 1  
    regen_matrix()
    pygame.display.flip()
    print(tick)
    clock.tick(60)
    pygame.display.update()
