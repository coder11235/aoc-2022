data = open("input.txt")

def sign(num):
    try:
        return num // abs(num)
    except:
        return 0

def move_knots(knots):
    for cur_i, (knot_x, knot_y) in list(enumerate(knots))[1:]:
        prev_x, prev_y = knots[cur_i-1]
        if abs(prev_x - knot_x) > 1 or abs(prev_y - knot_y) > 1:
            dir_x = sign(prev_x - knot_x)
            dir_y = sign(prev_y - knot_y)
            knots[cur_i] = (knot_x+dir_x, knot_y+dir_y)


knot_coords = [(0,0) for _ in range(10)]

last_k_past = set()
last_k_past.add((0, 0))


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
        head_x, head_y = knot_coords[0]
        head_x += mv_x
        head_y +=mv_y
        knot_coords[0] = (head_x, head_y)
        move_knots(knot_coords)
        last_k_past.add(knot_coords[9])


print(len(last_k_past))