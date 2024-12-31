from collections import Counter


def part1(inp):
    creatures = Counter(inp)
    potions = creatures["B"] + 3 * creatures["C"]
    return potions


creature_to_potion = {"B": 1, "C": 3, "D": 5}


def part2(inp):
    potions = 0
    for c1, c2 in zip(inp[::2], inp[1::2]):
        potions += creature_to_potion.get(c1, 0) + creature_to_potion.get(c2, 0)

        if "x" not in (c1, c2):
            potions += 2

    return potions


def part3(inp):
    line = inp.strip()
    potions = 0
    for c1, c2, c3 in zip(line[::3], line[1::3], line[2::3]):
        potions += (
            creature_to_potion.get(c1, 0)
            + creature_to_potion.get(c2, 0)
            + creature_to_potion.get(c3, 0)
        )

        num_x = sum(1 for c in (c1, c2, c3) if c == "x")
        if num_x == 1:
            potions += 2
        elif num_x == 0:
            potions += 6

    return potions
