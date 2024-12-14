import random
import os

# clear the console
os.system('clear')

REPEAT  = 1000000

def isDeadAfterShot(bullets, position):
    if (position in bullets):
        return True
    return False

def spinNTimes(bullets, barrelSize, n):
    [bullet1, bullet2] = bullets
    bullet1 = (bullet1 + n) % barrelSize
    bullet2 = (bullet2 + n) % barrelSize

    return [bullet1, bullet2]

def chooseAdjacentBullets(barrelSize):
    bullet1 = random.randrange(0, barrelSize)
    bullet2 = (bullet1 + 1) % barrelSize

    bullets = [bullet1, bullet2]
    return bullets

def chooseArbitraryBullets(barrelSize):
    bullet1 = random.randrange(0, barrelSize)
    bullet2 = random.randrange(0, barrelSize)

    while bullet2 == bullet1:
        bullet2 = random.randrange(0, barrelSize)

    bullets = [bullet1, bullet2]
    return bullets

def experiment(barrelSize, bulletsChoosalFunction):
    deadCountFirstSpin = 0
    deadCountNextShot = 0
    deadCountSpinAgain = 0

    for _ in range(REPEAT):
        bullets = bulletsChoosalFunction(barrelSize)

        numberOfSpins = random.randrange(1, barrelSize + 1)
        bullets = spinNTimes(bullets, barrelSize, numberOfSpins)
        initialPosition = random.randrange(0, barrelSize)

        if isDeadAfterShot(bullets, initialPosition):
            deadCountFirstSpin += 1
        else:
            # shot one again
            nextPosition = (initialPosition + 1) % barrelSize
            isDeadNextShot = isDeadAfterShot(bullets, nextPosition)
            if isDeadNextShot:
                deadCountNextShot += 1

            # spin the barrel and shoot
            numberOfSpins = random.randrange(1, barrelSize + 1)
            bullets = spinNTimes(bullets, barrelSize, numberOfSpins)
            position = random.randrange(0, barrelSize)
            isDeadAfterSpin = isDeadAfterShot(bullets, position)

            if isDeadAfterSpin:
                deadCountSpinAgain += 1

    return [deadCountFirstSpin, deadCountNextShot, deadCountSpinAgain]

def printTheData(barrelSize, exeprimentResults, experimentType):
    [deadCountFirstSpin, deadCountNextShot, deadCountSpinAgain] = exeprimentResults

    print("\n")
    print(f"------- {experimentType}: {barrelSize}) -------")
    print("\n")

    print(f"Chance of being alive after first shot is: { (REPEAT - deadCountFirstSpin)/REPEAT * 100 }%")
    print(f"Chance of dying after fist shot is: {deadCountFirstSpin/REPEAT * 100}%")

    print("--------------------------------------------------------------------------------------------------")
    deadCountNextShot = deadCountFirstSpin + deadCountNextShot
    print(f"Chance of dying after shooting again: {deadCountNextShot/REPEAT * 100}%")
    print(f"Chance of staying alive after shooting again: { (REPEAT - deadCountNextShot)/REPEAT * 100 }%")

    print("--------------------------------------------------------------------------------------------------")
    deadCountSpinAgain = deadCountFirstSpin + deadCountSpinAgain
    print(f"Chance of dying after spinning the barrel: {deadCountSpinAgain/REPEAT * 100}%")
    print(f"Chance of staying alive after spinning the barrel: { (REPEAT - deadCountSpinAgain)/REPEAT * 100 }%")

barrelSize = 6
adjenctBulletsPos = chooseAdjacentBullets(barrelSize)

experimentResult = experiment(barrelSize, chooseAdjacentBullets);
printTheData(barrelSize, experimentResult, "TWO ADJENCT BULLETS")

experimentResult  = experiment(barrelSize, chooseArbitraryBullets);
printTheData(barrelSize, experimentResult, "TWO ARBITRARY BULLETS")

barrelSize = 5
adjenctBulletsPos = chooseAdjacentBullets(barrelSize)

experimentResult = experiment(barrelSize, chooseAdjacentBullets);
printTheData(barrelSize, experimentResult, "TWO ADJENCT BULLETS")

experimentResult  = experiment(barrelSize, chooseArbitraryBullets);
printTheData(barrelSize, experimentResult, "TWO ARBITRARY BULLETS")
