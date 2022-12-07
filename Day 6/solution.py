input = open("Day 6/input.txt", "r").read()

def part1():

    for character in range(len(input)):
        letters = input[character : character + 4]
        if len(set(letters)) == len(letters):
            print(f"Part 1 answer : {character + 4}")
            break

def part2():

    for character in range(len(input)):
        letters = input[character : character + 14]
        if len(set(letters)) == len(letters):
            print(f"Part 2 answer : {character + 14}")
            break
 
part1(), part2()