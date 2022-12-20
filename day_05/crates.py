"""Advent of code day 5 "Crates"""

MOVE_INDEX = 0
FROM_INDEX = 1
TO_INDEX = 2
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

stacks = [[], [], [], [], [], [], [], [], []]

with open("puzzle_input.txt") as infile:
    for i in range(8):
        line = infile.readline().strip()
        count = 0
        for j in range(2, 36, 4):
            try:
                char = line[j - 1]
            except IndexError:
                char = " "
            if char in ALPHABET:
                stack_number = count
                stacks[count].append(char)
            count += 1
    infile.readline()
    infile.readline()
    step_count = 0
    for line in infile:
        line = line.split(" ")
        instruction = [int(line[1]), int(line[3]), int(line[5])]
        from_stack = stacks[instruction[FROM_INDEX] - 1]
        print(f"FROM: {from_stack}")
        elements = []
        for j in range(instruction[MOVE_INDEX]):
            element = from_stack.pop(0)
            elements.append(element)
        to_stack_number = instruction[TO_INDEX] - 1
        print(f"Elements: {elements}")
        stacks[to_stack_number] = elements + stacks[to_stack_number]
        print(f"TO: {stacks[to_stack_number]}")
        step_count += 1
        print(f"Step {step_count}")


for from_stack in stacks:
    try:
        print(from_stack[0], end="")
    except IndexError:
        print("Index error")
