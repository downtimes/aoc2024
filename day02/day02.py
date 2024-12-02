def parse(file):
    return [list(map(int, l.split())) for l in file]


def safe(line):
    # We ignore the case of only 1 or 0 elements here.
    assert len(line) >= 2
    diff = [x - y for (x, y) in zip(line[0::], line[1::])]
    return all(1 <= x <= 3 for x in diff) or all(-3 <= x <= -1 for x in diff)


def part1(parsed):
    return sum(map(safe, parsed))


def part2(parsed):
    def lessSafe(line):
        def oneDropped(line):
            for i in range(len(line)):
                yield line[:i] + line[i + 1 :]

        # Since we drop one and safe only handles lines with 2 elements,
        # this only works for lines with at least 3 elements.
        assert len(line) >= 3
        return any(safe(mod_line) for mod_line in oneDropped(line))

    return sum(map(lessSafe, parsed))


if __name__ == "__main__":
    with open("day02/input.txt", "r") as f:
        parsed = parse(f)

    p1 = part1(parsed)
    p2 = part2(parsed)
    print(p1, p2)
