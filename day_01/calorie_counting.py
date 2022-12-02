"""Advent of code 2022 day 1"""


with open("calories.txt") as infile:
    calorie_collection = infile.read()
    data = calorie_collection.split("\n\n")
    elves = [elf.split() for elf in data]
    elves = [[int(calorie) for calorie in elf] for elf in elves]
    highest_calories = max([sum(elf) for elf in elves])
    print(highest_calories)

