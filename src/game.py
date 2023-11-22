import os
from field import draw_field,jump,reset_dinosaur
from pytimedinput import timedInput
import time
def run():
    os.system('cls')
    draw_field(True)
    time.sleep(2)
    while True: 
        os.system('cls')
        
        draw_field()
        reset_dinosaur()
        txt,_ = timedInput('',timeout= 0.2)
        
        match txt:
            case ' ' | 'w':
                jump()