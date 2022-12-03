""" Advent of code day 3 Rucksack sorting"""

alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabet_to_values = {}

for i, letter in enumerate(alphabet, 1):
    alphabet_to_values[letter] = i
    alphabet_to_values[letter.upper()] = i + 26

with open("puzzle_input.txt") as infile:
    rucksacks = []
    elf_groups = []
    elves = []
    for line in infile:
        line = line.strip()
        elves.append(line)
        halfway = int(len(line) / 2)
        compartments = [line[:halfway], line[halfway:]]
        rucksacks.append(compartments)
    for i in range(0, len(elves), 3):
        elf_groups.append(elves[i:i+3])
duplicates = []
for compartments in rucksacks:
    duplicate = [item for item in compartments[0] if item in compartments[1]]
    duplicates.append(duplicate[0])
total = 0
for letter in duplicates:
    number = alphabet_to_values[letter]
    total += number
group_duplicates = []
group_total = 0
for group in elf_groups:
    group_duplicate = [item for item in group[0] if item in group[1] and item in group[2]]
    group_duplicates.append(group_duplicate[0])
for letter in group_duplicates:
    number = alphabet_to_values[letter]
    group_total += number
print(f"Total: {total}")
print(f"Group total: {group_total}")

