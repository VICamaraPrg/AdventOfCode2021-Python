"""
--- Day 3: Binary testCase ---

TODO
Remake the part 1 using the Counter.
Since I'm hardcoding what Counter does, without using it.
"""

from collections import Counter


with open("inputs/day-3.txt") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]


def part1(diagnostic, gammaRate="", epsilonRate="") :
    l = len(diagnostic)
    m = len(diagnostic[0])

    for s in range(m):
        map = dict()
        for n in range(0, l):
            if diagnostic[n][s] not in map:
                map[diagnostic[n][s]] = 1
            else:
                map[diagnostic[n][s]] += 1

        gammaRate += str(max(map, key = map.get))
        epsilonRate += str(min(map, key = map.get))

    return (int(gammaRate, 2) * int(epsilonRate, 2))


"""
--- Part Two ---

Using 2 equal inputs since both will get reduced.
"""

def part2(diagnostic):

    diagnostic2 = diagnostic
    loop = len(diagnostic[0])

    for i in range(loop):
        mostCommon = Counter([c[i] for c in diagnostic])

        if mostCommon["1"] < mostCommon["0"]:
            diagnostic = [j for j in diagnostic if j[i] == "0"]
        else:
            diagnostic = [j for j in diagnostic if j[i] == "1"]

    dioxid = diagnostic[0]

        
    for i in range(loop):
        mostCommon = Counter([c[i] for c in diagnostic2])

        if mostCommon["1"] < mostCommon["0"]:
            diagnostic2 = [j for j in diagnostic2 if j[i] == "1"]
        else:
            diagnostic2 = [j for j in diagnostic2 if j[i] == "0"]

        if diagnostic2:
            oxigen = diagnostic2[0]

        
    return (int(dioxid, 2) * int(oxigen,2))

print("Part 1:", part1(lines))
print("Part 2:", part2(lines))
