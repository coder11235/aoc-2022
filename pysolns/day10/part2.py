data = open("input.txt").read()

x_reg = 1
cycle_num = 0

crt = [['.' for _ in range(40)] for _ in range(6)]

def print_crt():
    for row in crt:
        print(''.join(row))
    print('')

def check_deb(cyc_num):
    vert_pos = cyc_num//40
    hor_pos = cyc_num%40
    if x_reg - 1 <= hor_pos <= x_reg + 1:
        crt[vert_pos][hor_pos] = '#'

for ln in data.splitlines():
    if ln == "noop":
        check_deb(cycle_num)
        cycle_num += 1
    else:
        _, num = ln.split(" ")
        num = int(num)
        for i in range(2):
            check_deb(cycle_num)
            cycle_num += 1
        x_reg += num

print_crt()