data = open("input.txt").read()

def parse(data: str):
    rows = []
    start = None
    end = None
    for line_num, line in enumerate(data.splitlines()):
        if 'S' in line:
            start = (line_num, line.index('S'))
        if 'E' in line:
            end = (line_num, line.index('E'))
        row = [ord(ch)-97 for ch in line.replace('E', 'z').replace('S', 'a')]
        rows.append(row)
    return rows, start, end

grid, start, end = parse(data)
vis = [[False]*len(grid[0]) for _ in range(len(grid))]

add = [(0,1), (0, -1), (1, 0), (-1, 0)]

def check_bounds(grid, i, j):
    return 0 <= i < len(grid) and 0 <= j < len(grid[0])


def solve(grid, end, frontier):
    count = 0
    while True:
        new_front = []
        for i, j in frontier:
            if (i, j) == end:
                return count
            if vis[i][j]:
                continue
            vis[i][j] = True
            cur_val = grid[i][j]
            for ai, aj in add:
                ni = i + ai
                nj = j + aj
                if not check_bounds(grid, ni, nj):
                    continue
                next_val = grid[ni][nj]
                if next_val <= (cur_val+1):
                    new_front.append((ni, nj))
        count += 1
        frontier = new_front

print(solve(grid, end, [start]))