def pad(grid):
    return (
        [["." for _ in range(len(grid[0]) + 2)]]
        + [["."] + row + ["."] for row in grid]
        + [["." for _ in range(len(grid[0]) + 2)]]
    )


def erode(grid, all_neighbors=False):
    if all_neighbors:
        displacements = [
            (dy, dx) for dy in range(-1, 2) for dx in range(-1, 2) if dy != 0 or dx != 0
        ]
        limit = 8
    else:
        displacements = [(1, 0), (0, 1), (0, -1), (-1, 0)]
        limit = 4

    next_grid = [[cell for cell in row] for row in grid]
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == ".":
                continue

            neighbors = [grid[y + dy][x + dx] for dy, dx in displacements]
            if neighbors.count("#") < limit:
                next_grid[y][x] = "."

    return next_grid


def solve(inp, all_neighbors=False):
    grid = [list(row.strip()) for row in inp.split("\n")]
    grid = pad(grid)

    answer = 0
    while True:
        excavate = sum(row.count("#") for row in grid)
        answer += excavate
        if excavate == 0:
            break
        grid = erode(grid, all_neighbors)

    return answer


def part1(inp):
    return solve(inp)


def part2(inp):
    return solve(inp)


def part3(inp):
    return solve(inp, all_neighbors=True)
