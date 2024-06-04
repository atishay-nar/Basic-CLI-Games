import logic as lc

# start the game
if __name__ == "__main__":
    mat = lc.start_game()

while True:
    # get user input
    x = input("Please press a command: ")

    if x == "W" or x == "w":
        mat, changed = lc.up_swipe(mat)
        # print game status
        status = lc.game_state(mat)
        print(status)

        # if the game continues add a 2 to the mat
        if status == "GAME NOT OVER":
            lc.add_two(mat)

        else:
            break

    # logic for other inputs
    elif x == "S" or x == "s":
        mat, changed = lc.down_swipe(mat)
        # print game status
        status = lc.game_state(mat)
        print(status)

        # if the game continues add a 2 to the mat
        if status == "GAME NOT OVER":
            lc.add_two(mat)

        else:
            break

    elif x == "A" or x == "a":
        mat, changed = lc.left_swipe(mat)
        # print game status
        status = lc.game_state(mat)
        print(status)

        # if the game continues add a 2 to the mat
        if status == "GAME NOT OVER":
            lc.add_two(mat)

        else:
            break

    elif x == "D" or x == "d":
        mat, changed = lc.right_swipe(mat)
        # print game status
        status = lc.game_state(mat)
        print(status)

        # if the game continues add a 2 to the mat
        if status == "GAME NOT OVER":
            lc.add_two(mat)

        else:
            break

    else:
        print("invalid input")
    for i in range(4):
        print(mat[i])
