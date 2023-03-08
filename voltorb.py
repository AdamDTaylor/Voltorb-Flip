# each row/ column has min 5 points, wherealll      squares = 1.
# if a square has two points, then that row or column must also have a voltorb, etc., etc.
# random number generator for row/column, if ? 5 then add voltorb, make 1 out of 4 1 slots into 2 slots

import random

grid = [[], [], [], [], []]
col_sums = []
row_sums = []

grid[0][3] = 5
print(grid[0][3])

def set_board():
    for x in range(len(grid)):
        col_sum = 0
        voltorb_count = 0
        for x in range(5):

            # dependent on level
            if(voltorb_count >= 6):
                random_num = random.randint(1, 3)

            else:
                random_num = random.randint(0, 3)
                if(random_num == 0):
                    voltorb_count +=1
                    
            grid[x].append(random_num)

    for rows in grid:
            print(rows)

        #     grid[x].append(random_num)
        #     col_sum += random_num
        # col_sums.append(col_sum)

    # for row in grid:
    #     row_sum = 0
    #     for y in range(5):
    #         row_sum += row[y]
    #     row_sums.append(row_sum)

    # for x in range(len(grid)):
    #     print(f"{grid[x]} {row_sums[x]}")
    # print(col_sums)


def set_level():
    return

set_board()