"""
--- Day 7: The Treachery of Whales ---
"""


f = "inputs/day-7.txt"

crabs = [int(c) for c in open(f).read().split(",")]

possibleAlign = len(input)

def calculateFuelCost(moves):
    return sum(range(1, moves + 1, 1))


def part1(fuel=[]):
    for align in range(max(crabs)):
        x = 0
        for crab in crabs:
            x += abs(crab - align)
        fuel.append(x)

    return min(fuel)

"""
--- Part Two ---
"""

def part2(fuel=[]):
    for align in range(max(crabs)):
        x = 0
        for crab in crabs:
            x += calculateFuelCost(abs(crab - align))
        fuel.append(x)

    return min(fuel)


print("Part 1:", part1())
print("Part 2:", part2())
