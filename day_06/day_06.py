"""Advent of Code day 6"""

with open("puzzle_input.txt") as infile:
    is_unique_nums = False
    numbers = infile.readline()
    while not is_unique_nums:
        group = []
        for i in range(len(numbers)):
            group = numbers[i:i + 14]
            if len(set(group)) == 14:
                is_unique_nums = True
                index = i
                break
    numbers = numbers[0:i+14]
    print(len(numbers))

