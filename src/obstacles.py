import random
from constants import FIELD_WIDTH, FIELD_HEIGHT
obstacles = []

def generate_obstacle():
    global obstacles
    if random.random() < 0.3:
        obstacles.append((FIELD_WIDTH - 2, FIELD_HEIGHT - 2))
        
def move_obstacles():
    global obstacles
    obstacles[:] = [(col - 1, row) for col, row in obstacles]
    
def check_collision(dinousaur_position: (float,float)):
    global obstacles
    return dinousaur_position in obstacles