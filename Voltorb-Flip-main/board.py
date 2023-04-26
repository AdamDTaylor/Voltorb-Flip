import random, pygame
from random import randint
from pygame import sprite
from game_tile import Tile
from level import level

base_grid = [[1,1,1,1,1], [1,1,1,1,1], [1,1,1,1,1], [1,1,1,1,1], [1,1,1,1,1]]
col_sums = []
row_sums = []

level_1 = level(
    potential_x2 = [3, 0, 5, 2, 4],
    potential_x3 = [1, 3, 0, 2, 1],
    potential_voltorb = [6, 6, 6, 6, 6]
    )
level_2 = level(
    potential_x2 = [1, 6, 3, 0, 5],
    potential_x3 = [3, 0, 2, 4, 1],
    potential_voltorb = [7, 7, 7, 7, 7]
)

level_3 = level(
    potential_x2 = [2, 7, 4, 1, 6],
    potential_x3 = [3, 0, 2, 4, 1],
    potential_voltorb = [8, 8, 8, 8, 8]
)

level_4 = level(
    potential_x2 = [3, 0, 8, 5, 2],
    potential_x3 = [3, 5, 0, 2, 4],
    potential_voltorb = [8, 8, 10, 10, 10]
)

level_5 = level(
    potential_x2 = [7, 4, 1, 9, 6],
    potential_x3 = [1, 3, 5, 0, 2],
    potential_voltorb = [10, 10, 10, 10, 10]
)

level_6 = level(
    potential_x2 = [3, 0, 8, 5, 2],
    potential_x3 = [4, 6, 1, 3, 5],
    potential_voltorb = [10, 10, 10, 10, 10]
)

level_7 = level(
    potential_x2 = [7, 4, 1, 9, 6],
    potential_x3 = [2, 4, 6, 1, 3],
    potential_voltorb = [10, 10, 13, 13, 10]
)

level_8 = level(
    potential_x2 = [0, 8, 5, 2, 7],
    potential_x3 = [7, 2, 4, 6, 3],
    potential_voltorb = [10, 10, 10, 10, 10]
)

levels = {
    "level_1": level_1,
    "level_2": level_2,
    "level_3": level_3,
    "level_4": level_4,
    "level_5": level_5,
    "level_6": level_6,
    "level_7": level_7,
    "level_8": level_8,
}




def pick_board(the_level: level):
    random_level = randint(0, 5)
    picked_level = the_level.boards[random_level]
    return picked_level



def get_random_index():
     random_row = randint(0, 4)
     random_col = randint(0,4)
     return random_row, random_col



    
def set_flip(grid, flip_value, amount):
    for values in range(amount):
        x, y = get_random_index()
        if grid[x][y] == 1:
            grid[x][y] = flip_value
        else:
             while grid[x][y] != 1:
                  x, y = get_random_index()
                  if grid[x][y] == 1:
                    grid[x][y] = flip_value
                    break
    return grid


def set_board(level_num):

    current_level = levels[level_num]
    board_values = pick_board(current_level)

    twos = board_values[0]
    threes = board_values[1]
    voltorb_num = board_values[2]

    with_voltorb = set_flip(base_grid, 0, voltorb_num)
    with_twos = set_flip(with_voltorb, 2, twos)
    full_board = set_flip(with_twos, 3, threes)

    return full_board
    

def convert_to_sprite(board):
    tiles = sprite.Group()
    current_tile = 1
    current_xCoord = 0
    current_yCoord = -80
    # converts board values to pygame sprites
    for x in range(len(board)):
        current_yCoord += 95
        current_xCoord = 0
        for y in range(len(board[x])):
            current_xCoord += 100
            value = board[x][y]
            tiles.add(Tile(current_tile, value, current_xCoord, current_yCoord))
            current_tile += 1
    
    # adds all sprites to a group
    # for x in range(len(board)):
    #     for y in range(len(board[x])):
    #         tiles.add(board[x][y])

    return tiles
     


