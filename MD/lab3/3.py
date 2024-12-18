from collections import defaultdict
import heapq

peopleInterests = [
    ["Music","Bieber","Internet","Movies"],
    ["Programming","T-Rex","Computers","Art"],
    ["Computers","Books","Football"],
    ["Football","Cats"],
    ["Internet","Videogames"],
    ["Programming","Movies","Cats"],
    ["Planes","Internet"],
    ["Cars","Internet"],
    ["Movies","Planes"],
    ["Theatre","Computers"],
    ["Internet","Theatre","Books"],
    ["Books","Cats","Programming"],
    ["Videogames","Bieber","Football"],
    ["Computers","Farming"],
    ["Theatre","Cars","Videogames","Politics"],
    ["Farming","Internet"],
    ["Beer","Theatre"],
    ["Farming","Cats","Books","Internet"],
    ["Programming","Theatre"],
    ["Farming","Computers"],
]

interests = [
    "Music", "Bieber", "Internet", "Movies", "Programming",
    "T-Rex", "Computers", "Art", "Books", "Football", "Cats",
    "Videogames", "Planes", "Cars", "Theatre", "Farming",
    "Politics", "Beer"
]

names = [
  "Caleb Hobby", "Alta Kennan", "Corrin Tally", "Leandro Eagan", "Otilia Laxson",
  "Ellie Francese", "Augustine Golub", "Elinore Orsborn", "Clarence Stalker",
  "Lili Houghton", "Monet Mccoy", "Angila Ellinger", "Sammie Womac",
  "Tiny Parkhurst", "Pearlie Moffet", "Cruz Perna", "Rebbecca Charlton",
  "Marita Tegeler", "Jarred Marrow", "Lorean Simcox"
]

data = [
  [0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1],
  [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
  [0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1],
  [0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1],
  [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1],
  [0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1],
  [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1],
  [0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0],
  [0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
  [0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
  [0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0],
  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
  [0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

influence = [
    2.7750000000000004, 9.9, 8.575000000000001, 6.65,4.525,
    8.149999999999999, 5.6499999999999995, 4.4, 3.4749999999999996,
    5.5, 5.550000000000001, 8.25, 8.5, 8.45,
    3.2750000000000004, 5.25, 7.7, 7.5249999999999995,
    7.65, 6.8999999999999995,
]

class Solution():
    friendsNumMap = {}
    connectionsMap = defaultdict(list)

    def __init__(self):
        self.createFriedsNumMap()
        self.createConnectionsMap()

    def createFriedsNumMap(self):
        s = len(data)
        for i in range(s):
            numOfFriends = sum(data[i])
            self.friendsNumMap[names[i]] = numOfFriends

    def getInterestToPeopleMap(self):
        map = {}
        for interest in interests:
            map[interest] = []

        for i in range(len(peopleInterests)):
            for j in range(len(peopleInterests[i])):
                map[peopleInterests[i][j]].append(i)

        return map

    def getRatingForBookPromo(self):
        interestToPeople = self.getInterestToPeopleMap()
        bookTopics = self.analyseBookTopics()
        influenceRating = self.getPeopleByInfluence()
        bookPromoRating = {}

        peopleToConcidingInterest = [0] * len(names)
        for interest, people in interestToPeople.items():
            if interest not in bookTopics: continue
            for pers in people:
                peopleToConcidingInterest[pers] += 1

        for pers, rating in influenceRating.items():
            bookPromoRating[pers] = rating * 0.2 * peopleToConcidingInterest[pers]

        bookPromoRating = dict(sorted(bookPromoRating.items(), key=lambda item: -item[1]))
        return bookPromoRating

    def createConnectionsMap(self):
        s = len(data)
        for i in range(s):
            for j in range(s):
                if data[i][j]:
                    self.connectionsMap[i].append(j)

    def getPeopleByInfluence(self):
        ratings = self.getPeopleByRating()
        influenceRating = {}
        for i, rating in ratings.items():
            influenceRating[i] = rating * 0.5 * influence[i]

        influenceRating = dict(sorted(influenceRating.items(), key=lambda item: -item[1]))
        return influenceRating

    def getPeopleByRating(self):
        ratings = {}
        for i in range(len(data)):
            distances = self.computeRating(i)
            rating = sum(d - 1 for d in distances if d != 0)
            ratings[i] = rating

        sortedByRanting = dict(sorted(ratings.items(), key=lambda item: -item[1]))
        return sortedByRanting

    def computeRating(self, person):
        s = len(data)
        distances = [float("inf")] * s
        distances[person] = 0

        queue = [(0, person)]
        heapq.heapify(queue)

        while queue:
            currDis, currNode = heapq.heappop(queue)

            if currDis > distances[currNode]:
                continue

            for neighbour in self.connectionsMap[currNode]:
                distance = currDis + 1

                if distance < distances[neighbour]:
                    distances[neighbour] = distance
                    heapq.heappush(queue, (distance, neighbour))
        return distances

    def analyseBookTopics(self, title="From T-Rex to Multi Universes: How the Internet has Changed Politics, Art and Cute Cats."):
        bookTopics = set()
        for interest in interests:
            if interest in title:
                bookTopics.add(interest)
        return bookTopics

    def getMostPopular(self):
        s = len(data)
        mostPopular = 0
        maxFriends = 0

        for i in range(s):
            if sum(data[i]) > maxFriends:
                maxFriends = sum(data[i])
                mostPopular = i

        return (mostPopular, maxFriends)

    def sortByFriends(self):
        sortedByFriends = dict(sorted(self.friendsNumMap.items(), key=lambda item: -item[1]))
        return sortedByFriends


solution = Solution()
print("\n--- 3.1 ---\n")
mostPopular, maxFriends = solution.getMostPopular()
print(f"The most popular person is {names[mostPopular]} with {maxFriends} friends")
print("\n--- 3.1 ---\n")

print("\n--- 3.2 ---\n")
sortedByFriends = solution.sortByFriends()
print(f"People sorted by friends: ")
for person, friends in sortedByFriends.items():
    print(f"{person} has {friends} friends")
print("\n--- 3.2 ---\n")

print("\n--- 3.3 ---\n")
ratings = solution.getPeopleByRating()
for i, rating in ratings.items():
    print(f"{names[i]}'s rating is {rating}")
print("\n--- 3.3 ---\n")


print("\n--- 3.4 ---\n")
influenceRating = solution.getPeopleByInfluence()
for i, rating in influenceRating.items():
    print(f"{names[i]}'s influence is {rating}")

print("\n--- 3.4 ---\n")

print("\n--- 3.5 ---\n")
bookTopics = solution.analyseBookTopics()
print("Interests related to the book: ")
for interest in bookTopics:
    print(interest)
print("\n--- 3.5 ---\n")

print("\n--- 3.6 ---\n")

peopleToConcidingInterest = solution.getRatingForBookPromo()
print("We should contact these people: ")
top5People = list(peopleToConcidingInterest.items())[:5]
for i, rating in top5People:
    print(f"{names[i]}'s ({rating})")

print("\n--- 3.6 ---\n")
