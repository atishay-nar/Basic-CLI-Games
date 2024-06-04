# import packages
import random as rd


# function to initialize the game
def start_game():
    # create empty matrix
    mat = []
    for i in range(4):
        mat.append([0] * 4)

    # give user command options
    print("Commands are as follows : ")
    print("'W' or 'w' : Move Up")
    print("'S' or 's' : Move Down")
    print("'A' or 'a' : Move Left")
    print("'D' or 'd' : Move Right")

    # create a new 2
    add_two(mat)

    for i in range(4):
        print(mat[i])
    return mat


# function to randomly add a two in an empty cell
def add_two(mat):
    # pick a random row and column
    r = rd.randint(0, 3)
    c = rd.randint(0, 3)

    # locate a blank cell
    while mat[r][c] != 0:
        r = rd.randint(0, 3)
        c = rd.randint(0, 3)

    # make that cell a two
    mat[r][c] = 2

    return


# function to determine if you have won
def game_state(mat):
    # check if any cell has 2048
    for i in range(4):
        for j in range(4):
            if mat[i][j] == 2048:
                return "WINNER!"

    # check if there are potential moves
    for i in range(3):
        for j in range(3):
            if mat[i][j] == mat[i][j + 1] or mat[i][j] == mat[i + 1][j]:
                return "GAME NOT OVER"

    for j in range(3):
        if mat[3][j] == mat[3][j + 1]:
            return "GAME NOT OVER"

    for i in range(3):
        if mat[i][3] == mat[i + 1][3]:
            return "GAME NOT OVER"

    return "Game Over"


# compress the matrix to the left to prepare to merge
def compress(mat):
    # bool to determine if a change happened
    changed = False

    # create blank mat
    new_mat = []
    for i in range(4):
        new_mat.append([0] * 4)

    for i in range(4):
        # position of the last empty square
        pos = 0
        # for every non empty cell in mat, moves it to the leftmost empty cell of new_mat
        for j in range(4):
            if mat[i][j] != 0:
                new_mat[i][pos] = mat[i][j]
                # if a cell has been moved than the mat has changed
                if j != pos:
                    changed = True
                # the next available cell is now one to the right
                pos += 1

    return new_mat, changed


# merge horizontally adjacent cells
def merge(mat):
    changed = False

    for i in range(4):
        # if two adjacent values are the same double one and make the other zero
        for j in range(3):
            if mat[i][j] == mat[i][j + 1] and mat[i][j] != 0:
                mat[i][j] = 2 * mat[i][j]
                mat[i][j + 1] = 0
                changed = True
    return mat, changed


# reversing a mat horizontaly
def reverse(mat):
    # create blank mat
    new_mat = []

    # flip it
    for i in range(4):
        new_mat.append([])
        for j in range(4):
            new_mat[i].append(mat[i][3 - j])

    return new_mat


# transposing a mat
def transpose(mat):
    # create blank mat
    new_mat = []
    for i in range(4):
        new_mat.append([0] * 4)

    # flip it
    for i in range(4):
        for j in range(4):
            new_mat[i][j] = mat[j][i]

    return new_mat


# left swipe
def left_swipe(grid):
    # first compress
    new_grid, changed1 = compress(grid)

    # then merge
    new_grid, changed2 = merge(new_grid)

    # compress again
    new_grid, temp = compress(new_grid)

    changed = changed1 or changed2

    return new_grid, changed


# right swipe
def right_swipe(grid):
    # first reverse
    new_grid = reverse(grid)

    # then left swipe
    new_grid, changed = left_swipe(new_grid)

    # then return the grid that has been reversed back
    new_grid = reverse(new_grid)

    return new_grid, changed


# up swipe
def up_swipe(grid):
    # first transpose
    new_grid = transpose(grid)

    # then left swipe
    new_grid, changed = left_swipe(new_grid)

    # then return the grid that has been transposed back
    new_grid = transpose(new_grid)

    return new_grid, changed


# down swipe
def down_swipe(grid):
    # first transpose
    new_grid = transpose(grid)

    # then right swipe
    new_grid, changed = right_swipe(new_grid)

    # then return the grid that has been transposed back
    new_grid = transpose(new_grid)
    return new_grid, changed
