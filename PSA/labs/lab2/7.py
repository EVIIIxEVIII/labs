import random
from collections import defaultdict
import matplotlib.pyplot as plt

# Write a program to carry out the following experiment.
# A coin is tossed 100 times and the number of heads that turn up is recorded.
# This experiment is then repeated 1000 times.
# Have your program plot a bar graph for the proportion of the 1000 experiments in which the number of heads is n, for each n in the interval [35, 65].
# Does the bar graph look as though it can be fit with a normal curve?

map = defaultdict(int)

for _ in range(1000):
    heads = 0

    for _ in range(100):
        heads += 1 if random.randrange(0, 2) == 1 else 0

    if heads >= 35 and heads <= 65:
        map[heads] += 1

numbers = list(map.keys())
times = list(map.values())

plt.bar(numbers, times)

plt.xlabel("Numbers")
plt.ylabel("Distribution")
plt.title("Numbers from 35 to 65 distribution")
plt.show()

print(map)
