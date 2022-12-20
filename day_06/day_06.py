"""Advent of Code day 6"""

with open("puzzle_input.txt") as infile:
    is_four_unique_nums = False
    numbers = infile.readline()
    while not is_four_unique_nums:
        quad = []
        for i in range(len(numbers)):
            quad = numbers[i:i+4]
            if len(set(quad)) == 4:
                is_four_unique_nums = True
                index = i
                break
    numbers = numbers[0:i+4]
    print(len(numbers))

