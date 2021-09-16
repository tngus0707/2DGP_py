from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x= 400
y = 90
angle = 0

while (1):
    angle += 1
    
    if angle == 360:
        angle = 0
        
    clear_canvas_now()
    grass.draw_now(400,30)
    
    mx = (math.cos((math.radians(angle))) * 4) + x
    my = (math.sin((math.radians(angle))) * 4) + y
    
    x = mx
    y = my
    
    character.draw_now(x, y)
    
    delay(0.01)

close_canvas()
