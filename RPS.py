import random, time
from time import sleep as sl


score = [0]*3
comp_list = ["R", "P", "S"]

print("\nLet's Play Rock Paper Scissors!")
sl(0.75)
print("\nDo you want to play?")
prompt = str(input("(Y/N): ")).upper()

while prompt != "Y" and prompt != "N":
    print("Please enter a valid input.")
    prompt = str(input("(Y/N): ")).upper()
    
while prompt == "Y":
    sl(0.75)
    print("\nChoose one: Rock(R), Paper(P), or Scissor(S)")
    user = str(input("(R/P/S): ")).upper()
    
    comp = random.choice(comp_list)
    
    sl(0.75)
    print("\nUser selects:",user)
    sl(0.75)
    print("\nComputer selects:",comp,"\n")
    sl(0.75)
    
    if user == comp:
        score[2] += 1
        print("Draw")
    elif user == "R" and comp == "S": 
        score[0] += 1
        print("User Wins!")
    elif user == "P" and comp == "R":
        score[0] += 1
        print("User Wins!")
    elif user == "S" and comp == "P":
        score[0] += 1
        print("User Wins!")
    elif user == "R" and comp == "P":
        score[1] += 1
        print("Computer Wins!")
    elif user == "P" and comp == "S":
        score[1] += 1
        print("Computer Wins!")
    elif user == "S" and comp == "R":
        score[1] += 1
        print("Computer Wins!")
        
    sl(0.75)
    print("\nScoreboard")
    sl(0.75)
    print("\nUser:",score[0],"\nComputer:",score[1],"\nDraw:",score[2])
    
    sl(0.75)
    print("\nDo you want to play again?")
    prompt = str(input("(Y/N): ")).upper()
    
else:
    sl(0.75)
    print("\nThanks for playing!")
    
    sl(0.75)
    print("\nFinal Scoreboard")
    sl(0.75)
    print("\nUser:",score[0],"\nComputer:",score[1],"\nDraw:",score[2])