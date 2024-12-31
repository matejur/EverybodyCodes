import os
import sys
import importlib


def get_input(quest, part):
    if os.path.exists(f"inputs/{quest}_{part}.txt"):
        with open(f"inputs/{quest}_{part}.txt") as f:
            return f.read().strip()

    print(f"Input for quest {quest} part {part}:")
    inp = ""
    while True:
        try:
            inp += input() + "\n"
        except EOFError:
            break

    with open(f"inputs/{quest}_{part}.txt", "w") as f:
        f.write(inp)

    return inp


if len(sys.argv) < 2:
    print("Usage: python run.py <quest>")
    sys.exit(1)

quest = f"{sys.argv[1]:0>2}"

try:
    solver = importlib.import_module(f"quest{quest}")
except ModuleNotFoundError:
    with open(f"quest{quest}.py", "w") as f:
        f.write(
            'def part1(inp):\n    return "Not implemented"\n\n\ndef part2(inp):\n    return "Not implemented"\n\n\ndef part3(inp):\n    return "Not implemented"\n'
        )
    print(f"Created quest file quest{quest}.py")
    sys.exit(1)

inp_1 = get_input(quest, "1")
print("Part 1:", solver.part1(inp_1))
inp_2 = get_input(quest, "2")
print("Part 2:", solver.part2(inp_2))
inp_3 = get_input(quest, "3")
print("Part 3:", solver.part3(inp_3))
