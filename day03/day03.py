import re


def parse(file):
    return list(
        re.findall(
            r"mul\(\d{1,3},\d{1,3}\)|don't\(\)|do\(\)", "".join(file.readlines())
        )
    )


def handleOne(mul):
    a, b = map(int, mul[4:-1].split(","))
    return a * b


def part1(parsed):
    return sum(handleOne(mul) for mul in parsed if mul.startswith("m"))


def part2(parsed):
    enabled = True
    sum = 0
    for ins in parsed:
        if ins.startswith("m") and enabled:
            sum += handleOne(ins)
        elif ins.startswith("do("):
            enabled = True
        else:
            enabled = False

    return sum


if __name__ == "__main__":
    with open("day03/input.txt", "r") as f:
        parsed = parse(f)

    p1 = part1(parsed)
    p2 = part2(parsed)
    print(p1, p2)
