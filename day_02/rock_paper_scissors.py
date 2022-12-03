"""Advent of code day 2 - Rock Paper Scissors"""

ABC_to_RPS = {"A": "rock", "B": "paper", "C": "scissors"}
XYZ_to_RPS = {"X": "lose", "Y": "draw", "Z": "win"}
option_to_loss = {"A": "C", "B": "A", "C": "B"}
option_to_draw = {"A": "A", "B": "B", "C": "C"}
option_to_win = {"A": "B", "B": "C", "C": "A"}

WIN = 6
DRAW = 3
LOSS = 0

ROCK = 1
PAPER = 2
SCISSORS = 3


with open("puzzle_input.txt") as infile:
    games = []
    for line in infile:
        game = [line[0], line[2]]
        games.append(game)
total = 0
for game in games:
    # if game[0] == "A" and game[1] == "Z" or game[0] == "B" and game[1] == "X" or game[0] == "C" and game[1] == "Y":
    #     total += LOSS
    # elif game[0] == "A" and game[1] == "X" or game[0] == "B" and game[1] == "Y" or game[0] == "C" and game[1] == "Z":
    #     total += DRAW
    # elif game[0] == "A" and game[1] == "Y" or game[0] == "B" and game[1] == "Z" or game[0] == "C" and game[1] == "X":
    #     total += WIN
    if game[1] == "X":
        total += LOSS
        game[1] = option_to_loss[game[0]]
    elif game[1] == "Y":
        total += DRAW
        game[1] = option_to_draw[game[0]]
    elif game[1] == "Z":
        total += WIN
        game[1] = option_to_win[game[0]]
    if game[1] == "A":
        total += ROCK
    elif game[1] == "B":
        total += PAPER
    elif game[1] == "C":
        total += SCISSORS
print(total)

