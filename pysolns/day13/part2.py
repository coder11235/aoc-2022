import json
from functools import cmp_to_key

data = open("input.txt").read()

def parse(data: str):
    ls = []
    for line in data.replace("\n\n", "\n").splitlines():
        ls.append(json.loads(line))
    return ls

parsed = parse(data)

parsed.append([[6]])
parsed.append([[2]])

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

def wrap_cmp(left,right):
    res = cmp(left, right)
    if res is None:
        return 0
    elif res:
        return -1
    else:
        return 1


sorted_lists = sorted(parsed, key=cmp_to_key(wrap_cmp))

print(
    (sorted_lists.index([[6]])+1) * (sorted_lists.index([[2]])+1)
    )