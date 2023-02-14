def game():
    return 64

score = game()
with open("highscore.txt") as f:
      highscore = int(f.read())
if score >highscore:
    with open("highscore.txt","w") as f:
        f.write(str(score))
