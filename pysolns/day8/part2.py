data = open("input.txt").read()

def parse(data):
    grid = [[int(ch) for ch in line] for line in data.splitlines()]
    return grid

grid = parse(data)

rows = len(grid)
cols = len(grid[0])

def recur_search(dir_v: int, dir_h: int, row: int, col: int, grid: int, height: int):
    next_pos_row = row+dir_v
    next_pos_col = col+dir_h
    if not ((0 <= next_pos_row < rows) and (0 <= next_pos_col < cols)):
        return 0
    next_height = grid[next_pos_row][next_pos_col]
    if next_height < height:
        return recur_search(dir_v, dir_h, next_pos_row, next_pos_col, grid, height) + 1
    else:
        return 1

def solve(grid):
    max_score = 0
    dirs = [(1,0), (-1,0), (0,1), (0,-1)]
    for row_num, row in enumerate(grid):
        for col_num, height in enumerate(row):
            score = 1
            for rd, cd in dirs:
                score *= recur_search(rd, cd, row_num, col_num, grid, height)
            if score > max_score:
                max_score = score
            
    print(max_score)

solve(grid)
