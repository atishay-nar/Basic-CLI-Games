import random as rd


def game_logic(wn, gu):
    cows = 0
    bulls = 0
    cwl = []

    if wn == gu:
        return True

    else:
        for i in range(4):
            if gu[i] == wn[i]:
                cows += 1
                cwl.append(gu[i])

        for n in set([i for i in gu]):
            if n in wn:
                blsa = wn.count(n) - cwl.count(n)
                pbls = gu.count(n) - cwl.count(n)
                blsad = 0

                for i in range(pbls):
                    if blsad < blsa:
                        bulls += 1
                        blsad += 1

        print(f"\nCows: {cows} Bulls: {bulls}")

        return False


def game():
    win = False
    attempts = 0
    win_num = "".join([rd.choice("1234567890") for i in range(4)])

    while True:
        guess = str(input(f"\nAttempt {attempts + 1}: Guess a 4 digit number\n\n>"))

        if len(guess) != 4:
            print("\nERROR: invalid input")

        else:
            attempts += 1
            win = game_logic(win_num, guess)

            if win == True:
                print(
                    f"\nCongratulations! The number was {win_num}! You won in {attempts} attempts!"
                )
                pa = str(input("\nWould you like to play again?\n\n[y/n]>")).lower()

                if pa == "y":
                    game()
                    break

                elif pa == "n":
                    print("\nThank you for playing!\n")
                    break

                else:
                    print("\nERROR")
                    break


if __name__ == "__main__":
    game()
