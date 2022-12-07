data = open("input.txt").read()

class Item:
    children: list["Item"]
    typ: str
    name: str
    size: int
    parent: "Item"

    def __init__(self, name, type, parent):
        self.name = name
        self.type = type
        self.size = None
        self.parent = parent
        self.children = []

    def find_child_with_name(self, name: str) -> "Item" :
        for child in self.children:
            if child.name == name:
                return child
        print("no such child", name, self)
        exit()

    def return_size(self):
        if self.size is None:
            self.size = self.calc_size()
        return self.size

    def calc_size(self):
        return sum(map(lambda x: x.return_size(), self.children))

def parse(data: str):
    parent = Item("/", "dir", None)
    current = parent
    for ln in data.splitlines()[1:]:
        if ln == "$ ls":
            continue
        if ln.startswith("$ cd"):
            _, name = ln.split("cd ")
            if name != "..":
                current = current.find_child_with_name(name)
            else:
                current = current.parent
        else:
            # add a new child
            child = None
            x, name = ln.split(" ")
            if x == "dir":
                child = Item(name, "dir", current)
            else:
                child = Item(name, "file", current)
                child.size = int(x)
            if current is not None:
                current.children.append(child)
            else:
                print("well fuck")
    return parent

parent = parse(data)

glob_total_sizes = 0
glob_least_size = float("inf")
glob_min_size_lim = 30000000-(70000000 - parent.return_size())
def solve_p(dir: Item):
    global glob_total_sizes
    global glob_least_size
    if dir.return_size() < 100000:
        glob_total_sizes += dir.return_size()
    if glob_min_size_lim < dir.return_size() < glob_least_size:
        glob_least_size = dir.return_size()
    for child in dir.children:
        if child.type == "dir":
            solve_p(child)

solve_p(parent)
print(glob_least_size)
