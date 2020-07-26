from game import Game

score = [0, 0]

for i in range(100):
    new_game = Game()
    if new_game.win():
        score[0] += 1
    else:
        score[1] += 1
print(score)