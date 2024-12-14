import random
import matplotlib.pyplot as plt

number_of_9 = 0
number_of_10 = 0

for _ in range(1_000_000):
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    dice3 = random.randint(1, 6)

    if dice1 + dice2 + dice3 == 9:
        number_of_9 += 1

    if dice1 + dice2 + dice3 == 10:
        number_of_10 += 1


values = [number_of_10, number_of_9]
labels = ["10", "9"]

plt.bar(labels, values, color=['blue', 'green'])
plt.ylabel('Value')
plt.title('Comparison of 10 vs 9')

plt.show()
