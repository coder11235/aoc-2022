from requests import get
import sys
import json
import os

day = sys.argv[1]

cookie = json.loads(open("secrets.json").read())["cookie"]

fldr = f"pysolns/day{day}"

os.mkdir(fldr)

r = get(f"https://adventofcode.com/2022/day/{day}/input", cookies={"session": cookie}, headers={"User-Agent": "personal use fetcher by udaykalyansreenivasa@gmail.com, https://github.com/coder11235/aoc-2022/blob/main/setupday.py"})

fl = open(f"{fldr}/input.txt", "w")
fl.write(r.text)

# one file solutions for the first few days
open(f"{fldr}/soln.py", "w")
open(f"{fldr}/sample.txt", "w")
