file = open("Day 8/input.txt").read()
grid = [[int(x) for x in line.strip()] for line in file.splitlines()]

def part1(): 

    #Create visibleTrees and assign outside trees.
    visibleTrees = 2 * len(grid) + 2 * (len(grid) - 2)

    for i in range(1, len(grid) - 1):
        for j in range(1, len(grid[0]) - 1):
            # check above
            if all(grid[line][j] < grid[i][j] for line in range(0, i)):
                visibleTrees += 1 
                continue
            # check below
            if all(grid[line][j] < grid[i][j] for line in range(i + 1, len(grid))):
                visibleTrees += 1
                continue
            # check right
            if all(grid[i][line] < grid[i][j] for line in range(j + 1, len(grid[i]))):
                visibleTrees += 1
                continue
            # check left
            if all(grid[i][line] < grid[i][j] for line in range(0, j)):
                visibleTrees += 1
                continue

    return visibleTrees

def part2(grid, i, j):
    
    # get above
    aboveScore = 0
    for k in range(i - 1, -1, -1):
        aboveScore += 1
        if grid[k][j] >= grid[i][j]:
            break

    # get below
    belowScore = 0
    for k in range(i + 1, len(grid)):
        belowScore += 1
        if grid[k][j] >= grid[i][j]:
            break

    # get left
    leftScore = 0
    for k in range(j - 1, -1, -1):
        leftScore += 1
        if grid[i][k] >= grid[i][j]:
            break
        
    # get right
    rightScore = 0
    for k in range(j + 1, len(grid[i])):
        rightScore += 1
        if grid[i][k] >= grid[i][j]:
            break

    return aboveScore * belowScore * leftScore * rightScore

part1Answer = part1()
part2Answer = max(part2(grid, i, j) for i in range(len(grid)) for j in range(len(grid[0])))

print(f"Part 1 answer : {part1Answer}")
print(f"Part 2 answer : {part2Answer}")