import json

data = open("input.txt").read()

def parse(data: str):
    ls = []
    for pair in data.split('\n\n'):
        pair_ls = []
        for line in pair.splitlines():
            pair_ls.append(json.loads(line))
        ls.append(pair_ls)
    return ls

parsed_pairs = parse(data)

def cmp(left, right):
    if type(left) == int and type(right) == int:
        if left == right:
            return None
        elif left < right:
            return True
        else:
            return False
    
    if type(left) == list and type(right) == int:
        right = [right]
    elif type(left) == int and type(right) == list:
        left = [left]

    for i in range(len(left)):
        li = left[i]
        try:
            ri = right[i]
        except:
            return False
        res = cmp(li, ri)
        if res is None:
            continue
        else:
            return res
    if len(left) == len(right):
        return None
    else:
        return True

ans = 0

for pair_num, pair in enumerate(parsed_pairs):
    if cmp(pair[0], pair[1]):
        ans += pair_num + 1

print(ans)