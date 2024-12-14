import random
import matplotlib.pyplot as plt

EXPER_NUM = 10_000

def do_exp(n):
    allDiff = 0
    for _ in range(EXPER_NUM):
        lunch = list(range(0, n))
        random.shuffle(lunch)

        lunchMap = [set() for _ in range(len(lunch))]

        for i in range(len(lunch)):
            prevPers = (i - 1) % len(lunch)
            nextPers = (i + 1) % len(lunch)
            lunchMap[lunch[i]] = {lunch[prevPers], lunch[nextPers]}

        dinner = list(range(0, n))
        random.shuffle(dinner)

        areAllDiff = True
        for i in range(len(dinner)):
            prevPers = (i - 1) % len(dinner)
            nextPers = (i + 1) % len(dinner)
            if dinner[prevPers] in lunchMap[dinner[i]] or dinner[nextPers] in lunchMap[dinner[i]]:
                areAllDiff = False
                break

        allDiff += 1 if areAllDiff else 0
    print(f"For {n} people, the probability is: ", allDiff / EXPER_NUM)
    return (allDiff / EXPER_NUM)

x = list(range(4, 100))
y = []

for i in range(4, 100):
    res = do_exp(i)
    y.append(res)

plt.figure(figsize=(10, 6))
plt.plot(x, y, marker='o', linestyle='-', color='b', label='Probability')

plt.title('Probability vs Number of Participants', fontsize=14)
plt.xlabel('Number of Participants (n)', fontsize=12)
plt.ylabel('Probability', fontsize=12)

plt.legend()
plt.show()
