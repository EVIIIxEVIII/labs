import random
import matplotlib.pyplot as plt

def europena_rullete(odd):
    ballAt = random.randrange(0, 37)

    if ballAt == 0:
        return False

    if odd:
        return (ballAt % 2) == 1
    return (ballAt % 2) == 0

balance = 10000
bet = 1

balance_history = [balance]
loss = 0
win = 0

for i in range(0, 1_000_000):
    if balance < bet:
        print(f"You gabled your life savings after {i} games, good job!")
        break

    balance -= bet
    if europena_rullete(True):
        balance += bet * 2
        bet = max(1, bet - 1)
        win += 1
    else:
        bet += 1
        loss += 1

    balance_history.append(balance)

x = range(0, len(balance_history))

plt.plot(x, balance_history)
plt.title("Graph of betting")
plt.xlabel("Bet number (x)")
plt.ylabel("Balance at that bet (y)")

plt.show()

values = [loss, win]
plt.bar(['Losses', 'Wins'], values, color=['red', 'green'])

plt.title('Wins vs Losses')
plt.xlabel('Result')
plt.ylabel('Count')

plt.show()

