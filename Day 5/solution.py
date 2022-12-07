from collections import deque 

def part1():

    with open('Day 5/input.txt', "r") as f:
       
        data = f.read().splitlines()
        stacks = {}
        for row in data:

            if "[" in row:
                for index, char in enumerate(row):
                    if (not (char == '[' or char == ']' or char == ' ')):
                        stackIndex = (index-1)//4 + 1
                        if (str(stackIndex) not in stacks):
                            stacks[str(stackIndex)] = deque([])
                        stacks[str(stackIndex)].appendleft(char)
            elif 'move' in row:
                rowSplit = row.split(' ')
                fromStack = rowSplit[3]
                toStack = rowSplit[5]
                quantity = rowSplit[1]
                for i in range(int(quantity)):
                    stacks[toStack].append(stacks[fromStack].pop())

        for i in range(len(stacks)):
            stack_key = str(i + 1)
            print(f"Part 1 answer : {stack_key, stacks[stack_key][-1]}")

def part2():

    from collections import deque 

    with open('Day 5/input.txt', "r") as f:
        read_data = f.read()

        rows = read_data.splitlines()

        stacks = {}

        for row in rows:

            if "[" in row:
                for index, char in enumerate(row):
                    if (not (char == '[' or char == ']' or char == ' ')):
                        stack_index = (index-1)//4 + 1
                        if (str(stack_index) not in stacks):
                            stacks[str(stack_index)] = deque([])
                        stacks[str(stack_index)].appendleft(char)
            elif 'move' in row:
                row_split = row.split(' ')
                from_stack = row_split[3]
                to_stack = row_split[5]
                quantity = row_split[1]
                crates_to_move = []
                for i in range(int(quantity)):
                    crates_to_move.append(stacks[from_stack].pop())
                for i in range(int(quantity)):
                    stacks[to_stack].append(crates_to_move.pop())

        for i in range(len(stacks)):
            stack_key = str(i + 1)
            print(f"Part 2 answer : {stack_key, stacks[stack_key][-1]}")

part1(), part2()