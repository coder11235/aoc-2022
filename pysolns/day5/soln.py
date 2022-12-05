from collections import deque
data = list(open("input.txt").read().splitlines())

def parse(data):
    rows = [deque([]) for _ in range(9)]
    for ln in reversed(data[:8]):
        for index, char in enumerate(ln):
            if (index-1)%4 == 0 and char != " ":
                rows[(index-1)//4].append(char)
    cmds = []
    for ln in data[10:]:
        _, num, _, fro, _, to = ln.split(' ')
        cmds.append((int(num), int(fro), int(to)))
    return rows, cmds

def part1(rows,cmds):
    for num, fro, to in cmds:
        for _ in range(num):
            rows[to-1].append(rows[fro-1].pop())
    print("part1: ", end="")
    for i in rows:
        print(i.pop(), end="")
    print("")

def part2(rows,cmds):
    for num, fro, to in cmds:
        picked = []
        for _ in range(num):
            picked.append(rows[fro-1].pop())
        for i in reversed(picked):
            rows[to-1].append(i)
    print("part2: ", end="")
    for i in rows:
        print(i.pop(), end="")

rows1, cmds = parse(data)
rows2 = [x.copy() for x in rows1]
part1(rows1,cmds)
part2(rows2, cmds)