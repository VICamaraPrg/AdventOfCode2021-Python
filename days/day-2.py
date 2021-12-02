"""
--- Day 2: Dive! ---
"""

import re

with open("inputs/day-2.txt") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

def part1(instructions, depth=0, horizontal=0):
    for instruction in instructions: 
        order = re.findall(r"^([a-z]{1}).+\s+(\d+)", instruction)
        command = order[0][0]
        value = int(order[0][1])

        if command == "f":
            horizontal += value
        elif command == "u":
            depth -= value
        elif command == "d":
            depth += value

    return (depth * horizontal)

"""
--- Part Two ---
"""

def part2(instructions, depth=0, horizontal=0, aim=0):
    for instruction in instructions: 
        order = re.findall(r"^([a-z]{1}).+\s+(\d+)", instruction)
        command = order[0][0]
        value = int(order[0][1])

        if command == "f":
            horizontal += value
            depth += (aim * value)
        elif command == "u":
            aim -= value
        elif command == "d":
            aim += value

    return (depth * horizontal)


print("Part 1:", part1(lines))
print("Part 2:", part2(lines))