"""
--- Day 1: Sonar Sweep ---
"""

with open("inputs/day-1.txt") as file:
    lines = file.readlines()
    lines = [int(line.rstrip()) for line in lines]


def part1(sonar, increases = 0):
    for depth in range(1, len(sonar)):
        if sonar[depth] > sonar[depth - 1]:
            increases += 1

    return increases


"""
--- Part Two ---
"""

def part2(sonar, increases = 0, pos = 0, groupSum = []):

    # Loop through the sonar data making groups of 3.
    # Since we start at pos 1 (to compare with pos 0):
    # We also must to end at pos -1, otherwise will
    # cause an Out of Range error.

    for depth in range(1, len(sonar) - 1):
        currentSum = 0
        for group in range(3):
            currentSum += sonar[pos + group]
        groupSum.append(currentSum)
        pos += 1

    # Loop through the sums and compare.
    for sum in range(1, len(groupSum)):
        if groupSum[sum] > groupSum[sum - 1]:
            increases += 1

    return increases


print("Part 1:", part1(lines))
print("Part 2:", part2(lines))