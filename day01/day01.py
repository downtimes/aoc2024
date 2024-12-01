from collections import Counter
from itertools import tee

def parse(lines):
    return zip(*[map(int, line.split()) for line in lines])

def p1(parsed):
    l, r = parsed
    l1s = sorted(l)
    l2s = sorted(r)
    return sum(abs(l1 - l2) for (l1, l2) in zip(l1s, l2s))

def p2(parsed):
    l, r = parsed
    c = Counter(l)
    return sum(id * c[id] for id in r)

if __name__ == '__main__':
    with open("day01/input.txt", "r") as f:
        parsed = parse(f.readlines())
        i1, i2 = tee(parsed)
        p1 = p1(i1)
        p2 = p2(i2)
        print(p1, p2)