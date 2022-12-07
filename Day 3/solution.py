import string
file = open("Day 3/input.txt", "r")
lines = file.read().splitlines()

def part1():

    result = 0
    for line in lines:
        halfway = len(line)//2
        letter = set(line[:halfway]).intersection(line[halfway:]) 
        result += string.ascii_letters.index(''.join(letter)) + 1
    print(f"Part 1 answer : {result}")

def part2():

    first = 0; second = 1; third = 2; result = 0

    while third <= len(lines):
        for letter in set(lines[first]):
            if letter in lines[second] and letter in lines[third]:
                result += string.ascii_letters.index(letter) + 1   
        first += 3; second += 3; third += 3
    print(f"Part 2 answer : {result}")
    
part1(); part2()