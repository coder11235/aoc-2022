data = open("input.txt").read()

class Monkey:
    items: list[int]
    # to be run in eval
    operation: str
    test: int
    true_monkey: int
    false_monkey: int
    monkey_num: int
    inspections: int

def parse(data: str):
    monkeys = []
    for monkey_raw in data.split('\n\n'):
        st, op,test, monkey_true, monkey_false = tuple(map(
            lambda l: l.strip(),
            monkey_raw.splitlines()[1:]
        ))
        monkey = Monkey()
        monkey.items = list(map(lambda x: int(x), st.split(": ")[1].split(', ')))
        monkey.operation = op.split('= ')[1]
        monkey.test = int(test.split("by ")[1])
        monkey.true_monkey = int(monkey_true.split("monkey ")[1])
        monkey.false_monkey = int(monkey_false.split("monkey ")[1])
        monkey.inspections = 0
        monkeys.append(monkey)
    return monkeys

monkeys: list[Monkey] = parse(data)

for round_num in range(20):
    for mon in monkeys:
        for old in mon.items:
            mon.inspections += 1
            worry_level = eval(mon.operation)
            worry_level = worry_level // 3
            if worry_level%mon.test == 0:
                monkeys[mon.true_monkey].items.append(worry_level)
            else:
                monkeys[mon.false_monkey].items.append(worry_level)
        mon.items = []

inspec = list(map(lambda m: m.inspections, monkeys))
inspec.sort()

print(inspec[-1]*inspec[-2])