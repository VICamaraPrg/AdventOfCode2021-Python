"""
--- Day 4: Giant Squid ---
"""

import re

bingoSheet = []
f = "inputs/day-4.txt"

# Read the numbers drawn (1st line). Regex.
with open(f) as file: 
   line = file.readline()
   numbersDrawn = re.findall(r"(\d+)", line)

# Read the bingo sheets, comprenhension list.
sheets = [[c.split() for c in r.split("\n")] for r in open(f).read().strip().split("\n\n")][1:]

# Diagonal is not required (I think), so just check for X and Y.
def XYCheck(sheet):
    # Horizontal check.
    for x in range(5):
        possibleWinner = True
        for y in range(5):
            if sheet[x][y] != "X":
                possibleWinner = False
        if possibleWinner:
            return True
    # Vertical check.
    for x in range(5):
        possibleWinner = True
        for y in range(5):
            if sheet[y][x] != "X":
                possibleWinner = False
        if possibleWinner:
            return True

    return False

# NOTE: This function can be used or not.
# On the second function, you can extract part 1 and part 2.
def markNumbersP1(notmarkedSum=0):
    for n in numbersDrawn:
        for sheet in sheets:
            for numbers in sheet:
                for x in range(len(numbers)):
                    if numbers[x] == n:
                        numbers[x] = "X"
                if XYCheck(sheet):
                    for numbers in sheet:
                        for y in numbers:
                            if y != "X":
                                notmarkedSum += int(y)

                    return (notmarkedSum * int(n))


"""
--- Part Two ---
"""

def markNumbersP2(listWinners=[], winnerSheets=set()):
    for n in numbersDrawn:
        for x in range(len(sheets)):
            sheet = sheets[x]
            for numbers in sheet:
                for y in range(len(numbers)):
                    if numbers[y] == n:
                        numbers[y] = "X"

            if XYCheck(sheet) and (x not in winnerSheets):
                notmarkedSum=0
                for numbers in sheet:
                    for z in numbers:
                        if z != "X":
                            notmarkedSum += int(z)

                winnerSheets.add(x)
                listWinners.append(notmarkedSum * int(n))

    return listWinners[0], listWinners[-1]


def part1And2():
    part1, part2 = markNumbersP2()
    print("Part 1:", part1)
    print("Part 2:", part2)

part1And2()