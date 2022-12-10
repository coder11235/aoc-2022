data = open("sample.txt").read()

x_reg = 1

to_show = [20, 60, 100,140, 180, 220]
cycle_num = 1

sig_sum = 0

def check_deb(cyc_num):
    global sig_sum
    if cyc_num in to_show:
        sig_sum += cyc_num*x_reg

for ln in data.splitlines():
    # during cycle
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

print(sig_sum)