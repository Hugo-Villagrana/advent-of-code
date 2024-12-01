from collections import defaultdict


def main():
    leftLocationDict = defaultdict(int)
    rightLocationDict = defaultdict(int)
    with open("input.txt") as f:
        for line in f:
            parse = line.strip().split(" ")
            left, right = int(parse[0]), int(parse[-1])

            leftLocationDict[left] += 1
            rightLocationDict[right] += 1

    score = 0
    for key in leftLocationDict.keys():
        score += leftLocationDict[key] * (key * rightLocationDict[key])

    print(score)


main()
