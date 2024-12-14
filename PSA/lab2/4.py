import random
import math

def random_cord():
    angle = random.random() * 2 * math.pi
    y = math.sin(angle);
    x = math.cos(angle);

    return (x, y, angle)

def comp_ang(p1, p2, p3):
    vec1 = (p1[0] - p2[0], p1[1] - p2[1])
    vec2 = (p3[0] - p2[0], p3[1] - p2[1])

    dot = vec1[0]*vec2[0] + vec1[1]*vec2[1]
    magnitude_prod = math.sqrt(vec1[0]**2 + vec1[1]**2) * math.sqrt(vec2[0]**2 + vec2[1]**2)

    return math.degrees(math.acos((dot)/(magnitude_prod)))

convex_num = 0
less_than_120 = 0

for _ in range(1_000_000):
    arr = []
    for _ in range(4):
        arr.append(random_cord())

    arr.sort(key = lambda x: x[2])

    p1 = arr[0]
    p2 = arr[1]
    p3 = arr[2]
    p4 = arr[3]

    angle1 = comp_ang(p1, p2, p3)
    angle2 = comp_ang(p4, p1, p2)
    angle3 = comp_ang(p3, p4, p1)
    angle4 = comp_ang(p2, p3, p4)

    if angle1 < 180 and angle2 < 180 and angle3 < 180 and angle4 < 180:
        convex_num += 1

    if angle1 < 120 and angle2 < 120 and angle3 < 120 and angle4 < 120:
        less_than_120 += 1

print(f"The prob that the thing is convex is {convex_num / 1_000_000}")
print(f"The prob that the thing has all angles less than 120 is {less_than_120 / 1_000_000}")
