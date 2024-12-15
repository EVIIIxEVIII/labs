import random
import matplotlib.pyplot as plt

def europena_rullete(odd):
    ballAt = random.randrange(0, 37)

    if ballAt == 0:
        return False

    if odd:
        return (ballAt % 2) == 1
    return (ballAt % 2) == 0

def n_fib_num(n, memo = {}):
    if n in memo:
        return memo[n]

    if n == 0:
        memo[0] = 0
        return 0

    if n == 1:
        memo[1] = 1
        return 1

    num = n_fib_num(n - 2, memo) +  n_fib_num(n - 1, memo)
    memo[n] = num
    return num

balance = 1000.0
balance_history = [balance]

fib_n = 1

win = 0
loss = 0

for _ in range(0, 100000):
    bet = n_fib_num(fib_n)
    if balance < bet:
        print("You gabled your life savings, good job!")
        break

    balance -= bet
    if europena_rullete(True):
        balance += bet * 2
        fib_n = max(1, fib_n - 2)
        win += 1
    else:
        fib_n = min(fib_n + 1, 50)
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
