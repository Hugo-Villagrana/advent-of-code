import re


def solution2():
    with open("input.txt") as f:
        total = 0
        skip = False
        for line in f:
            matches = re.findall(r"don\'t\(\)|do\(\)|mul\([0-9]+,[0-9]+\)", line)
            for match in matches:
                print(match)
                if match == "do()" or match == "don't()":
                    skip = match == "don't()"
                    continue

                if not skip:
                    [lhs, rhs] = re.findall("[0-9]+", str(match))
                    total += int(lhs) * int(rhs)
        return total


print(solution2())
