"""
--- Day 6: Lanternfish ---
"""

import re

f = "inputs/day-6.txt"
with open(f) as file: 
   line = file.readline()
   initialState = re.findall(r"(\d+)", line)

initialState = [int(n) for n in initialState]

def newDay(toAppend=0):
    r = len(initialState)
    for c in range(r):
        if initialState[c] == 0:
            toAppend += 1

    return toAppend

# NOTE: This is a bad solving!
# To get part 2, it took aorund 5 minutes.
def parts():
    for x in range(80):
        append = newDay()
        for i in range(len(initialState)):
            if initialState[i] != 0:
                initialState[i] -= 1
            elif initialState[i] == 0:
                initialState[i] = 6

        if append > 0:
            for z in range(append):
                initialState.append(8)

    print("Fish:", len(initialState))


parts()