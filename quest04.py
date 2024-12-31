def part1(inp):
    nails = list(map(int, inp.split()))
    lowest = min(nails)

    return sum(nail - lowest for nail in nails)


def part2(inp):
    nails = list(map(int, inp.split()))
    lowest = min(nails)

    return sum(nail - lowest for nail in nails)


def part3(inp):
    nails = list(map(int, inp.split()))
    median = sorted(nails)[len(nails) // 2]

    return sum(abs(nail - median) for nail in nails)
