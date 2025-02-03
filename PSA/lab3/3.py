import random

def chooseRandomSeat(seats):
    availableSeats = [i for i, seat in enumerate(seats) if seat is None]
    return random.choice(availableSeats)

def simulate():
    TRIES = 1_000_000

    lastSeatsRandomly = 0
    for _ in range(TRIES):
        seats: list[int|None] = [None] * 100

        randomSeat = random.randint(0, 99)
        seats[randomSeat] = 0

        for i in range(98):
            if seats[i] is None:
                seats[i] = i
            else:
                randomSeat = chooseRandomSeat(seats)
                seats[randomSeat] = i

        if seats[99] is not None:
            lastSeatsRandomly += 1

    print(f"Tries {TRIES} number of times")
    print(f"The last person will seat in their seat with probability {1 - lastSeatsRandomly/TRIES}")


simulate()
