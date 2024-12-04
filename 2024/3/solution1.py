import re


def solution1():
    with open("input.txt") as f:
        sum = 0
        for line in f:
            matches = re.findall(r"mul\([0-9]+,[0-9]+\)", line)
            for match in matches:
                print(match)
                [lhs, rhs] = re.findall("[0-9]+", str(match))
                print(int(lhs), int(rhs))
                sum += int(lhs) * int(rhs)
    return sum


print(solution1())
