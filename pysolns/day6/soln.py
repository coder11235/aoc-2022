data = open('input.txt').read()
# data = open('sample.txt').read()

def part1():
    for i in range(len(data)):
        if len(set(data[i:i+4])) == 4:
            print(i+4)
            break

def part2():
    for i in range(len(data)):
        if len(set(data[i:i+14])) == 14:
            print(i+14)
            break

part2()