"""Advent of code 2022 day 1"""


with open("calories.txt") as infile:
    calorie_collection = infile.read()
    data = calorie_collection.split("\n\n")
    elves = [elf.split() for elf in data]
    elves = [[int(calorie) for calorie in elf] for elf in elves]
    total_calories_per_elf = [sum(elf) for elf in elves]
    total = 0
    for i in range(3):
        highest_calorie = max(total_calories_per_elf)
        print("Max: ", highest_calorie)
        calorie = total_calories_per_elf.pop(total_calories_per_elf.index(highest_calorie))
        total += calorie
    print("Total:", total)
