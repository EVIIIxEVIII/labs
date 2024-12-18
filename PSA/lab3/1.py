import random
import math

def simulate(arrivalRate, numTrials):
  totalWaitTime = 0
  for _ in range(numTrials):
    waitTime = random.expovariate(arrivalRate)
    totalWaitTime += waitTime
  return totalWaitTime / numTrials

arrivalRate = 6
numTrials = 10000

averageWaitTime = simulate(arrivalRate, numTrials)
print(f"{averageWaitTime * 60:.2f} minutes")
