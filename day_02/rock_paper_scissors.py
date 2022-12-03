"""Advent of code day 2 - Rock Paper Scissors"""

ABC_to_RPS = {"A": "rock", "B": "paper", "C": "scissors"}
XYZ_to_RPS = {"X": "rock", "Y": "paper", "Z": "scissors"}

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
    if game[0] == "A" and game[1] == "Z" or game[0] == "B" and game[1] == "X" or game[0] == "C" and game[1] == "Y":
        total += LOSS
    elif game[0] == "A" and game[1] == "X" or game[0] == "B" and game[1] == "Y" or game[0] == "C" and game[1] == "Z":
        total += DRAW
    elif game[0] == "A" and game[1] == "Y" or game[0] == "B" and game[1] == "Z" or game[0] == "C" and game[1] == "X":
        total += WIN
    if game[1] == "X":
        total += ROCK
    elif game[1] == "Y":
        total += PAPER
    elif game[1] == "Z":
        total += SCISSORS
print(total)

