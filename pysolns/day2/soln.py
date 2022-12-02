data = open("input.txt").read()


def soln1():
    arr1 = ["A", "B", "C"]
    arr2 = ["X", "Y", "Z"]
    win_arr = ["Y", "Z", "X"]
    points = 0
    for ln in data.splitlines():
        point_r = 0
        l, r = ln.split(" ")
        if arr1.index(l) == arr2.index(r):
            point_r = 3
        elif arr1.index(l) == win_arr.index(r):
            point_r = 6
        point_r += arr2.index(r) + 1
        points += point_r
    print(points)

def soln2():
    arr1 = ["A", "B", "C"]
    points = 0
    for ln in data.splitlines():
        point_r = 0
        l, r = ln.split(" ")
        l = arr1.index(l)
        throw = None
        if r == "X":
            if l == 0:
                throw = 2
            else:
                throw = l - 1
        elif r == "Y":
            throw = l
            point_r = 3
        else:
            if l == 2:
                throw = 0
            else:
                throw = l + 1
            point_r = 6
        point_r += throw + 1
        points += point_r
    print(points)

soln1()
soln2()
