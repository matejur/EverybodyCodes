import re


def part1(inp):
    words, sentence = inp.split("\n\n")
    words = words.split(":")[1].split(",")

    answer = 0
    for word in words:
        pattern = re.compile(word)
        answer += len(pattern.findall(sentence))

    return answer


def part2(inp):
    words, *sentences = inp.split("\n\n")
    words = words.split(":")[1].split(",")

    answer = 0
    for sentence in sentences:
        counted = [False for _ in range(len(sentence))]
        for word in words:
            pattern = re.compile(word)
            for match in pattern.finditer(sentence):
                for i in range(match.start(), match.end()):
                    counted[i] = True
            for match in pattern.finditer(sentence[::-1]):
                for i in range(match.start(), match.end()):
                    counted[len(sentence) - i - 1] = True
        answer += counted.count(True)

    return answer


def part3(inp):
    words, sentences = inp.split("\n\n")
    sentences = sentences.split("\n")
    words = words.split(":")[1].split(",")

    grid = [list(row.strip()) for row in sentences]
    scales = [[False for _ in grid[0]] for _ in grid]

    for y, row in enumerate(grid):
        for x, char in enumerate(row):
            for word in words:
                if word[0] != char:
                    continue

                for dx, dy in [(1, 0), (0, 1), (0, -1), (-1, 0)]:
                    for i in range(1, len(word)):
                        nx, ny = x + dx * i, y + dy * i
                        if nx < 0:
                            nx += len(grid[0])
                        if nx >= len(grid[0]):
                            nx -= len(grid[0])
                        if ny < 0 or ny >= len(grid):
                            break

                        if grid[ny][nx] != word[i]:
                            break
                    else:
                        for i in range(len(word)):
                            nx, ny = x + dx * i, y + dy * i
                            if nx < 0:
                                nx += len(grid[0])
                            if nx >= len(grid[0]):
                                nx -= len(grid[0])

                            scales[ny][nx] = True

    return sum([row.count(True) for row in scales])
