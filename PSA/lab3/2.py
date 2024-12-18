import math
import random

def getMaxXY(angle):
    MAX_X = math.cos(angle) * 10
    MAX_Y = math.sin(angle) * 10
    return (MAX_X, MAX_Y)

def getRandomPointInUpperPart():
    randomAngleUpperPart = random.random() * math.pi
    MAX_X, MAX_Y = getMaxXY(randomAngleUpperPart)

    x = random.random() * MAX_X
    y = random.random() * MAX_Y

    return (x, y)

def isInRightHalf(point):
    if point[0] > 0:
        return True
    return False

def getDistanceFromCenter(point):
    return math.sqrt(point[0]**2 + point[1]**2)

def isNearPoint(point, randomPoint, proximity):
    normalizedCords = (randomPoint[0] - point[0], randomPoint[1] - point[1])
    distance = getDistanceFromCenter(normalizedCords)
    return distance <= proximity

def simulate():
    TRIES = 1_000_000
    inRightHalf = 0
    distFromCentLessThan5 = 0
    distFromCentMoreThan5 = 0
    nearPoint = 0

    for _ in range(TRIES):
        point = getRandomPointInUpperPart()

        if isInRightHalf(point):
            inRightHalf += 1

        if getDistanceFromCenter(point) > 5:
            distFromCentMoreThan5 += 1

        if getDistanceFromCenter(point) < 5:
            distFromCentLessThan5 += 1

        if isNearPoint((0, 5), point, 5):
            nearPoint += 1

    print(f"The dart is in the right half: {inRightHalf/TRIES}")
    print(f"The dart distance from center > 5: {distFromCentMoreThan5/TRIES}")
    print(f"The dart distance from center < 5: {distFromCentLessThan5/TRIES}")
    print(f"The dart distance to (0, 5): {nearPoint/TRIES}")

simulate()
