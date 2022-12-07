with open("Day 4/input.txt", "r") as f:
    lines = [line.strip().split(",") for line in f.readlines()]

def part1():

    result = 0

    for pair in lines:
        elf1Start, elf1End = [int(x) for x in pair[0].split("-")]
        elf2Start, elf2End = [int(x) for x in pair[1].split("-")]

        if elf1Start > elf2Start:
            elf1Start, elf1End = [int(x) for x in pair[1].split("-")]
            elf2Start, elf2End = [int(x) for x in pair[0].split("-")]

        if elf1Start <= elf2Start and elf1End >= elf2End:
            result += 1
        elif elf1Start == elf2Start:
            result += 1

    print(f"Part 1 answer : {result}")

def part2():

    result = 0

    for pair in lines:
    
        elf1Start, elf1End = [int(x) for x in pair[0].split("-")]
        elf2Start, elf2End = [int(x) for x in pair[1].split("-")]

        if elf1Start > elf2Start:
            elf1Start, elf1End = [int(x) for x in pair[1].split("-")]
            elf2Start, elf2End = [int(x) for x in pair[0].split("-")]

        if elf1End < elf2Start:
            result += 1

    print(f"Part 2 answer : {len(lines) - result}")

part1(), part2()