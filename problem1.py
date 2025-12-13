# ...existing code...
import random

def game():
    print("You are playing game ")
    score = random.randint(1, 100)
    with open("highscore.txt") as f:
        highscore = f.read()
        if highscore != "":
            highscore = int(highscore)
        else:
            highscore = 0

    print(f"your score is {score}")
    if score > highscore:
        print("You have the highest score")
        with open("highscores.txt", "w") as f:
            f.write(str(score))
    else:
        print(f"Highest score is {highscore}")
    return score

game()