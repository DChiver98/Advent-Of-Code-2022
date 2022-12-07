data = open("Day 1/input.txt", "r")
lines = data.read().splitlines()

def part1():

    count = 0; max = 0

    for line in lines: 
        if line.strip() == "":
            if count > max:
                max = count
                count = 0
            else:
                count = 0
        else:
            count += int(line)
    print(f"Part 1 answer : {max}")

def part2():

    count = 0; elves = []

    for line in lines: 
        if line.strip() == "":
            elves.append(count)
            count = 0
        else:
            count += int(line)

    print(f"Part 2 answer : {elves[-1] + elves[-2] + elves[-3]}")

part1(), part2()