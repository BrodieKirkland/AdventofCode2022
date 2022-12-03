""" Advent of code day 3 Rucksack sorting"""

alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabet_to_values = {}

for i, letter in enumerate(alphabet, 1):
    alphabet_to_values[letter] = i
    alphabet_to_values[letter.upper()] = i + 26

with open("puzzle_input.txt") as infile:
    rucksack_collection = []
    for line in infile:
        line = line.strip()
        halfway = int(len(line) / 2)
        rucksacks = [line[:halfway], line[halfway:]]
        rucksack_collection.append(rucksacks)
duplicates = []
for rucksacks in rucksack_collection:
    duplicate = [item for item in rucksacks[0] if item in rucksacks[1]]
    duplicates.append(duplicate[0])
total = 0
for letter in duplicates:
    number = alphabet_to_values[letter]
    total += number
print(total)
