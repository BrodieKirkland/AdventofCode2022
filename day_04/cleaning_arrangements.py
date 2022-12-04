"""Advent of code day 4 Cleaning arrangements"""

with open("puzzle_input.txt") as infile:
    elf_pairs = []
    for line in infile:
        elf_pair = line.strip().split(",")
        elf_pair = [elf.split("-") for elf in elf_pair]
        elf_pair = [[int(number) for number in elf] for elf in elf_pair]
        elf_pairs.append(elf_pair)
total = 0
full_overlaps = []
partial_overlaps = []
print(elf_pairs)
for elf_pair in elf_pairs:
    if (elf_pair[0][0] <= elf_pair[1][0]) and (elf_pair[0][1] >= elf_pair[1][1]):
        full_overlaps.append(elf_pair)
    elif (elf_pair[0][0] >= elf_pair[1][0]) and (elf_pair[0][1] <= elf_pair[1][1]):
        full_overlaps.append(elf_pair)
    if (elf_pair[0][0] in range(elf_pair[1][0], elf_pair[1][1] + 1)) or (
            elf_pair[0][1] in range(elf_pair[1][0], elf_pair[1][1] + 1)):
        partial_overlaps.append(elf_pair)
    elif (elf_pair[1][0] in range(elf_pair[0][0], elf_pair[0][1] + 1)) or (
            elf_pair[1][1] in range(elf_pair[0][0], elf_pair[0][1] + 1)):
        partial_overlaps.append(elf_pair)

print(len(full_overlaps))
print(len(partial_overlaps))

