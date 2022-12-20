"""Advent of Code day 6"""

group_size = 14
with open("puzzle_input.txt") as infile:
    is_unique_nums = False
    numbers = infile.readline()
    while not is_unique_nums:
        group = []
        for i in range(len(numbers)):
            group = numbers[i:i + group_size]
            if len(set(group)) == group_size:
                is_unique_nums = True
                index = i
                break
    numbers = numbers[0:i+group_size]
    print(len(numbers))

