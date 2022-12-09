data = open("input.txt")

def sign(num):
    try:
        return num // abs(num)
    except:
        return 0

def move_tail(head_x, head_y, tail_x, tail_y):
    if abs(head_x - tail_x) > 1 or abs(head_y - tail_y) > 1:
        dir_x = sign(head_x - tail_x)
        dir_y = sign(head_y - tail_y)
        tail_x += dir_x
        tail_y += dir_y
    return tail_x, tail_y


head_y = 0
head_x = 0
tail_x = 0
tail_y = 0

tail_coords = set()
tail_coords.add((0, 0))

for ln in data:
    dr, num = ln.split(' ')
    num = int(num)
    mv_x, mv_y = 0, 0
    if dr == 'L':
        mv_x -= 1
    elif dr == 'R':
        mv_x += 1
    elif dr == 'D':
        mv_y -= 1
    else:
        mv_y += 1
    for i in range(num):
        head_x += mv_x
        head_y +=mv_y
        tail_x, tail_y = move_tail(head_x, head_y, tail_x, tail_y)
        tail_coords.add((tail_x, tail_y))


print(len(tail_coords))