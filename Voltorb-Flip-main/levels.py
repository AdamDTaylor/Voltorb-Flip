import random, pygame
from random import randint
from pygame import sprite
from game_tile import Tile

base_grid = [[1,1,1,1,1], [1,1,1,1,1], [1,1,1,1,1], [1,1,1,1,1], [1,1,1,1,1]]
col_sums = []
row_sums = []

     

# def level_1():
#     for x in range(len(grid)):
#         col_sum = 0
#         voltorb_count = 0
#         for x in range(5):

#             if(voltorb_count >= 6):
#                 random_num = random.randint(1, 3)

#             else:
#                 random_num = random.randint(0, 3)
#                 if(random_num == 0):
#                     voltorb_count +=1
                    
#             grid[x].append(random_num)

#     for rows in grid:
#             print(rows)
     
# def level_2()
     
# def level_3()
     
# def level_4()
     
# def level_5()
     
# def level_6()
     
# def level_7()
     
# def level_8()

def set_board(twos, threes, voltorb_num):
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
     



convert_to_sprite(set_board(3, 1, 6))