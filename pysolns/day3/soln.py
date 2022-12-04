data = open("input.txt").read()

def getpri(inp: str):
    if inp.islower():
        return ord(inp) - 96
    else:
        return ord(inp) - 38

def soln1():
    total_pri = 0
    for ln in data.splitlines():
        cm = set(ln[:len(ln)//2]) & set(ln[len(ln)//2:])
        for i in cm:
            total_pri += getpri(i)
    print("soln 1:",total_pri)

def soln2():
    total_pri = 0
    lst = list(data.splitlines())
    i = 0
    while i < len(lst):
        s1 = set(lst[i])
        s2 = set(lst[i+1])
        s3 = set(lst[i+2])
        common = (s1 & s2 & s3).pop()
        total_pri += getpri(common)
        i += 3
    print("soln 2:", total_pri)

soln1()
soln2()
