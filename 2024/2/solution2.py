# Notes: Each line of input is a report, each number on line is a level.
# The levels are either all increasing or all decreasing.
# Any two adjacent levels differ by at least one and at most three.


def is_valid_level(level: list[int]):
    is_monotonic = all(level[i] > level[i - 1] for i in range(1, len(level))) or all(
        level[i] < level[i - 1] for i in range(1, len(level))
    )
    if not is_monotonic:
        return 0

    for i in range(len(level)):
        if i - 1 > 0 and (
            abs(level[i] - level[i - 1]) > 3 or abs(level[i] - level[i - 1]) < 1
        ):
            return 0

        if i + 1 < len(level) - 1 and (
            abs(level[i] - level[i + 1]) > 3 or abs(level[i] - level[i + 1]) < 1
        ):
            return 0

    return 1


def permutation(level: list[int]):
    if is_valid_level(level):
        return 1

    for i in range(len(level)):
        if is_valid_level(level[:i] + level[i + 1 :]):
            return 1

    return 0


def solution2():
    valid_report_count = 0
    with open("input.txt") as f:
        for report in f:
            level = list(int(level) for level in report.strip().split(" "))
            valid_report_count += permutation(level)
    return valid_report_count


print(solution2())
