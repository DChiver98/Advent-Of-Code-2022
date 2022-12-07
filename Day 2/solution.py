file = open("Day 2/input.txt", "r")
lines = file.read().splitlines()

def part1():

    myChoices = {"X" : 1, "Y" : 2, "Z" : 3} 
    myScore = 0

    for line in lines:
        myScore += myChoices[line[2]]
        if line[0] == "A" and line[2] == "Y" or line[0] == "B" and line[2] == "Z" or line[0] == "C" and line[2] == "X":
            myScore += 6
        elif line[0] == "A" and line[2] == "X" or line[0] == "B" and line[2] == "Y" or line[0] == "C" and line[2] == "Z":
            myScore += 3

    print(f"Part 1 answer : {myScore}")
    
def part2():

    myScore = 0

    for line in lines:
        #lose
        if line[2] == "X":
            if line[0] == "A":
                myScore += 3
            elif line[0] == "B":
                myScore += 1
            elif line[0] == "C":
                myScore += 2
        #draw
        if line[2] == "Y":
            if line[0] == "A":
                myScore += 4
            if line[0] == "B":
                myScore += 5
            if line[0] == "C":
                myScore += 6
        #win
        if line[2] == "Z":
            if line[0] == "A":
                myScore += 8
            if line[0] == "B":
                myScore += 9
            if line[0] == "C":
                myScore += 7

    print(f"Part 2 answer : {myScore}")

part1(), part2()