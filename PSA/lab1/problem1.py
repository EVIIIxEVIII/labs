import random
import matplotlib.pyplot as plt
import numpy as np
import os

# clear the console
os.system('clear')

BIG_NUMBER_OF_PLAYS = 10_000
SMALL_NUMBER_OF_PLAYS = 10

big_outcomes = []

for i in range(BIG_NUMBER_OF_PLAYS):
    money = 2

    outcome = random.randint(0, 1)
    while outcome != 1:
        money *= 2
        outcome = random.randint(0, 1)

    big_outcomes.append(money)

big_avg = sum(big_outcomes) / len(big_outcomes)
print(f"The average return for 10 million games is: {big_avg}")
# I would pay arround $20, because most of the times
# average of 10 million games is arround $20 to $30

print("\n\n")

small_outcomes = []
small_averages = []

for y in range(100_000):
    outcomes_small_num_games = []
    for z in range(SMALL_NUMBER_OF_PLAYS):
        money = 2

        while random.randint(0, 1) != 1:
            money *= 2

        outcomes_small_num_games.append(money)

    average_of_10 = sum(outcomes_small_num_games) / SMALL_NUMBER_OF_PLAYS;
    small_averages.append(average_of_10)
    small_outcomes.append(sum(outcomes_small_num_games))

small_avg = sum(small_outcomes) / len(small_outcomes)

print(f"The average return for {SMALL_NUMBER_OF_PLAYS} games is: ", small_avg)
print(f"The median of average outcomes is: {np.median(small_averages)}")

print(f"The median profit of {SMALL_NUMBER_OF_PLAYS} games is: {np.median(small_outcomes)}")
print(f"The maximum profit was: {max(small_outcomes)}")


filtered_small_avg = [x for x in small_averages if x <= 1000]
# filtered_small_avg = small_outcomes

plt.subplot(1, 2, 1)
plt.hist(filtered_small_avg, bins=100, alpha=0.7, edgecolor='black')
plt.title("Distribution of Median Average Outcomes")
plt.xlabel("Average Outcome Per Game")
plt.ylabel("Frequency")

plt.show()

# according to the graph and the number the program returned I would
# pay around $4 to play the game so in the end I have around $18 if I was
# proposed to play this game 10 times.
