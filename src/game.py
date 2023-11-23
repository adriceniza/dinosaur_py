import time
import os
from field import draw_field,jump,reset_dinosaur
from pytimedinput import timedInput
from obstacles import generate_obstacle,move_obstacles,obstacles,check_collision

def run():
    jumping = False
    timeout_jumping = 0
    
    timeout_jumping_time = 3
    
    os.system('cls')
    draw_field([],True)
    time.sleep(2)
    while True: 
        os.system('cls')
        
        draw_field(obstacles)
        
        if not jumping:
            reset_dinosaur()
            
        txt,_ = timedInput('',timeout= 0.2)
        
        if jumping:
             timeout_jumping -= 1
             if timeout_jumping < 1:
                 jumping = False
        
        match txt:
            case ' ' | 'w':
                jump()
                jumping = True
                timeout_jumping = timeout_jumping_time
                
                
        generate_obstacle()
        move_obstacles()

        from field import DINOSAUR_POSITION
        if check_collision(DINOSAUR_POSITION):
            print("Game Over! You collided with an obstacle.")
            break