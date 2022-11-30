from requests import get
import sys
import json
import os

day = sys.argv[1]

cookie = json.loads(open("secrets.json").read())["cookie"]

fldr = "pysolns/day{day}"

os.mkdir(fldr)

r = get(f"https://adventofcode.com/2022/day/{day}/input", cookies={"session": cookie})

fl = open(f"{fldr}/input.txt", "w")
fl.write(r.text)

open(f"{fldr}/day1.py", "w")
open(f"{fldr}/day2.py", "w")
open(f"{fldr}/sample.txt", "w")
