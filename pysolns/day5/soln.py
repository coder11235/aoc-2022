from collections import deque
data = open("input.txt").read()

def parse(data):
    rows = [deque([]) for _ in range(9)]
    for i in data.splitlines()[:8]:

