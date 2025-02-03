import random

insideBlack = 0
TOTAL_TRIES = 1_000_000
balance = 10_000

for _ in range(TOTAL_TRIES):
    balance -= 0.25

    x = random.random() * 8
    y = random.random() * 8

    wholeX = int(x)
    wholeY = int(y)

    blCorner = [wholeX, wholeY]
    urCorner = [wholeX + 1, wholeY + 1]

    if (wholeX + wholeY) % 2 != 0:
        continue

    if (
        (x - 0.25 >= blCorner[0] and x + 0.25 <= urCorner[0])
        and
        (y - 0.25 >= blCorner[1] and y + 0.25 <= urCorner[1])
    ):
        insideBlack += 1
        balance += 1

print(f"Total number of tries {TOTAL_TRIES}")
print(f"The chance is { insideBlack / TOTAL_TRIES }")
print(f"The balance is: { balance }")
print(f"The game is not fair!")


