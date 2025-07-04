import random
import time

auto = ["rock", "paper", "scissor"]

score = 0
print("Welcome to Rock, Paper, Scissor game!\n")

while True:
    man = input("Enter the object (rock, paper, scissor): ").lower()
    comp = random.choice(auto)
    print(f"Computer chose: {comp}")
    time.sleep(1)
    if comp == man:
        print("Replay\n")
    elif comp == "rock":
        if man == "paper":
            print("You win\n")
            score += 1
        elif man == "scissor":
            print("You lose\n")
            break
    elif comp == "paper":
        if man == "rock":
            print("You lose\n")
            break
        elif man == "scissor":
            print("You win\n")
            score += 1
    elif comp == "scissor":
        if man == "rock":
            print("You win\n")
            score += 1
        elif man == "paper":
            print("You lose\n")
            break
time.sleep(2)
print("Game Over!")
print(f"Your score is: {score}")