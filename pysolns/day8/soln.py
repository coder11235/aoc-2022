data = open("input.txt").read()

def parse(data):
    grid = [[int(ch) for ch in line] for line in data.splitlines()]
    vis = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
    return grid, vis

grid, vis = parse(data)

def solve(grid, vis):
    # check from left / right
    for line_num, line in enumerate(grid):
        # left
        greatest_left = -1
        for row_num, height in enumerate(line):
            if height > greatest_left:
                vis[line_num][row_num] = True
                greatest_left = height
        # right
        greatest_right = -1
        for row_num, height in reversed(list(enumerate(line))):
            if height > greatest_right:
                vis[line_num][row_num] = True
                greatest_right = height

    # check from top / bottom
    for col_num in range(len(grid[0])):
        # top
        greatest_top = -1
        for row_num in range(len(grid)):
            height = grid[row_num][col_num]
            if height > greatest_top:
                vis[row_num][col_num] = True
                greatest_top = height
        
        # bottom
        greatest_bot = -1
        for row_num in reversed(range(len(grid))):
            height = grid[row_num][col_num]
            if height > greatest_bot:
                vis[row_num][col_num] = True
                greatest_bot = height

    print("day1: ", sum([sum(line) for line in vis]))

solve(grid, vis)
