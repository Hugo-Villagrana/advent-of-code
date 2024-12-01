# Each location from input is a locationId
# Must match the distance from smallest left dataset to smallest right dataset

# Maybe the lists are only off by a small amount! To find out, pair up the numbers and measure how far apart they are.
# Pair up the smallest number in the left list with the smallest number in the right list,
# then the second-smallest left number with the second-smallest right number, and so on.


# Assumptions
# left and right locations will always be the same length


def question1():
    leftLocations = []
    rightLocations = []
    with open("input.txt") as f:
        for line in f:
            parse = line.strip().split(" ")
            left, right = int(parse[0]), int(parse[-1])

            leftLocations.append(left)
            rightLocations.append(right)

    leftLocations.sort()
    rightLocations.sort()

    quantity = 0
    for l, r in zip(leftLocations, rightLocations):
        quantity += abs(l - r)

    print(quantity)


question1()
