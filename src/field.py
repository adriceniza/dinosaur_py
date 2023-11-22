from constants import FIELD_WIDTH,FIELD_HEIGHT,WALL,DINOSAUR,BACKGROUND,INSTRUCTIONS_TEXT

CELLS = [(col,row) for row in range(FIELD_HEIGHT) for col in range(FIELD_WIDTH)]
LIMITS = [(0, FIELD_HEIGHT-1),(0, FIELD_WIDTH-1)]

FLOOR_POSITION = ((FIELD_WIDTH/2)-1, FIELD_HEIGHT-2)
AIR_POSITION = ((FIELD_WIDTH/2)-1, FIELD_HEIGHT-4)

ON_AIR = False

DINOSAUR_POSITION = FLOOR_POSITION

def jump():
    global ON_AIR, DINOSAUR_POSITION
    if not ON_AIR:
        DINOSAUR_POSITION = AIR_POSITION
        ON_AIR = True

def reset_dinosaur():
    global ON_AIR, DINOSAUR_POSITION
    DINOSAUR_POSITION = FLOOR_POSITION
    ON_AIR = False

def get_positions_from_instructions(instructions):
    positions = []
    start_col = ((FIELD_WIDTH/2) - len(instructions))

    for col_offset, char in enumerate(instructions):
        col = start_col + col_offset
        row = FIELD_HEIGHT // 2 
        positions.append((col, row, char))

    return positions

def draw_field(show_instructions_text=False):
    
    instructions_positions = get_positions_from_instructions(INSTRUCTIONS_TEXT)
    
    for cell in CELLS:
        
        col = cell[0]
        row = cell[1]

        if show_instructions_text:
            for inst_col, inst_row, char in instructions_positions:
                if col == inst_col and row == inst_row:
                    print(char, end='')

        if col in (0, FIELD_WIDTH-1) or row in (0, FIELD_HEIGHT-1):
            if(col == FIELD_WIDTH-1):
                print(WALL)
            else:
                print(WALL, end='')
        elif col == DINOSAUR_POSITION[0] and row == DINOSAUR_POSITION[1] and not show_instructions_text:
            print(DINOSAUR, end='')
        else:
            print(BACKGROUND, end='')