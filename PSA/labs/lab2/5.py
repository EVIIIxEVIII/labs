import random

# 0 boy, 1 girl
until_first_boy = []
for _ in range(1_000_000):
    tries = 0
    while True:
        tries += 1
        gender = random.randrange(0, 2)

        if gender == 0:
            break

    until_first_boy.append(tries)

print(f"Avg number of children with only one boy: {sum(until_first_boy) / len(until_first_boy)}")


until_boy_and_girl = []
for _ in range(1000):
    tries = 0
    girl_present = False
    boy_present = False

    while True:
        tries += 1
        gender = random.randrange(0, 2)

        if gender == 0:
            boy_present = True

        if gender == 1:
            girl_present = True

        if girl_present and boy_present:
            break

    until_boy_and_girl.append(tries)

print(f"Avg number of children with at least one boy and at least one girl: { sum(until_boy_and_girl) / len(until_boy_and_girl) }")
