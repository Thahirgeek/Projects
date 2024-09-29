import random

user_score = 0
computer_score = 0

picks = ["rock", "paper", "scissor"]

while user_score != 3 and computer_score != 3:
    user_pick = input("Enter your pick (Rock, Paper or Scissor) or q to quit the game: ").lower()
    if user_pick == "q":
        exit()
    elif user_pick not in picks:
        print("Enter a valid pick")
    else:
        num = random.randint(0,2)
        computer_pick = picks[num]

        if user_pick == "rock" and computer_pick == "scissor":
            print("🙂 YOU WIN!!  Computer picked: " + computer_pick)
            user_score += 1
        elif user_pick == "paper" and computer_pick == "rock":
            print("🙂 YOU WIN!!  Computer picked: " + computer_pick)
            user_score += 1
        elif user_pick == "scissor" and computer_pick == "paper":
            print("🙂 YOU WIN!!  Computer picked: " + computer_pick)
            user_score += 1
        elif user_pick == computer_pick:
            print("😒 TIE !! Computer picked: " + computer_pick)
        else:
            print("🙁 YOU LOSE!!  Computer picked: " + computer_pick)
            computer_score += 1
        print("Your score: " + str(user_score))
        print("Computer's score: " + str(computer_score) + "\n")

print("* * * * * * * * * * * ")
if(user_score == 3):
    print("🎉 YOU win 🎉 by " + str(user_score) + ":" + str(computer_score))
else:
    print("🤖 COMPUTER wins 🤖 by " + str(computer_score) + ":" + str(user_score))
print("* * * * * * * * * * * ")