data= open("input.txt")

total_cals = []

cal = 0
for i in data.read().splitlines():
    if i.isdigit():
        cal += int(i)
    else:
        total_cals.append(cal)
        cal = 0

total_cals.sort()

print(f"soln1: {total_cals[-1]}")

print(f"soln2: {sum(total_cals[-3:])}")
