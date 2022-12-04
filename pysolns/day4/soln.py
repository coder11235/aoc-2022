import re
data = open("input.txt").read()

def parse(inp):
    return map(
            lambda line: list(map(
                lambda x: int(x),
                re.split(r"-|,",line)
            )),
            inp.splitlines()
        )

def soln1():
    proc = parse(data)
    c = 0
    for i in proc:
        l1, l2, r1,r2 = i
        if (l1 >= r1) ^ (l2 >= r2) or l1 == r1 or l2 == r2:
            c += 1
    print(c)

def soln2():
    proc = parse(data)
    c = 0
    for i in proc:
        l1, l2, r1,r2 = i
        if (l1 <= r2) ^ (l2 <= r1) or l1 == r2 or r1 == l2:
            c += 1
    print(c)

soln2()
