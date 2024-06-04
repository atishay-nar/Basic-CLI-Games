import random, time
from time import sleep as sl

choices = ["MONDAY", "ALBERT", "BASKETBALL", "SOCCER", "COMPUTER", "PYTHON", "PEACE", "YELLOW","PILLOW", "EXOTIC", "ETERNAL", "GLASS", "CASTLE", "BEAUTIFUL", "COBRA", "SPIDER", "TRENCH", "MAXIMUM"]

print("\nLet's play Hangman!")
sl(0.75)
print("\nDo you want to play?")
prompt = str(input("(Y/N): ")).upper()

while prompt != "Y" and prompt != "N":
    sl(0.75)
    print("Please enter a valid input.")
    prompt = str(input("(Y/N): ")).upper()

while prompt == "Y":
    
    error_count = 0

    word = random.choice(choices)

    display = ["-"]*len(word)

    while word != "".join(display) and error_count < 6:
        temp_display = display.copy()
        
        sl(0.75)
        print("\nThe word is:\n","".join(display))
        
        sl(0.75)
        guess = str(input("Guess a letter: ")).upper()
    
        while len(guess) != 1:
            sl(0.75)
            guess = str(input("Please enter exactly one letter: ")).upper()
            
        for i in range(len(word)):
            if guess == word[i]:
                display[i] = guess
    
        if temp_display == display:
            sl(0.75)
            print("\n",guess,"was not a letter in the word")
            error_count+=1

    if "".join(display) == word:
        sl(0.75)
        print("\nCongratulations! You win! The word was:",word)
    else:
        sl(0.75)
        print("\nYou lose. The words was:",word)
        
    sl(0.75)
    print("\nDo you want to play again?")
    prompt = str(input("(Y/N): ")).upper()

sl(0.75)
print("\nThanks for playing!")
