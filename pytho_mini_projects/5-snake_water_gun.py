import random

option = ["snake","gun","water"]
round = 0
user_score = 0
comp_score = 0
n=0
for i in range(1,6):
    round +=1
    print(f".........this is round {round}........")

    user = input(""" choose btwn:
             1.snake
             2.water
             3.gun

             enter your choice(1,2,3): """)
    computer = random.choice(option)
    if user == "1" and computer == "snake":
        print(f"round {round} draw")
    elif user == "2" and computer == "water":
        print(f"round {round} draw")
    elif user == "3" and computer == "gun":
        print(f"round {round} draw")
    elif user == "1" and computer == "water":
        print(f"round {round} user wins the round")
        user_score +=1
    elif user == "2" and computer == "gun":
        print(f"round {round} user wins the round")
        user_score +=1

    elif user == "3" and computer == "snake":
        print(f"round {round} user wins the round")
        user_score +=1

    elif user == "1" and computer == "gun":
        print(f"round {round} computer wins the round")
        comp_score +=1
    elif user == "2" and computer == "snake":
        print(f"round {round} computer wins the round")
        comp_score +=1
    elif user == "3" and computer == "water":
        comp_score +=1
        print(f"round {round} computer wins the round")
    else :
        print("invalid choice")

print("\n.........this is a final score...........")

if user_score > comp_score:
    print(f"user wins the game by {user_score} rounds")
elif comp_score > user_score:
    print(f"computer wins the game by {comp_score} rounds")
else:
    print("the game is draw")

with open("score.txt","+a") as f:
    content = f.write(f"\n....this is the water snake gun game record.....\n user score is {user_score} \n computer score is {comp_score}")
    print("\n.........the score has been updated in the file : score.txt.......")