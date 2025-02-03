import json
from collections import defaultdict
import nltk
from nltk.tokenize import word_tokenize
nltk.download('punkt_tab')

class Solution():
    def __init__(self):
        self.loadData()
        self.loadWordsEmotions()

    tweets = {}
    wordToEmotion = {}

    def loadData(self):
        with open('tweets.json', 'r') as file:
            self.tweets = json.load(file)

    def loadWordsEmotions(self):
        with open('AFINN-111.txt', 'r') as file:
            wordsByEmotion = file.read()

        lines = wordsByEmotion.split("\n")
        for line in lines:
            word, score = line.split("\t")
            self.wordToEmotion[word] = score

        print(self.wordToEmotion)


    def getHashtagsByFreq(self):
        allHashtagsFreq = defaultdict(lambda: 0)

        for tweet in self.tweets:
            splitText = tweet['text'].split()
            for word in splitText:
                if word.startswith("#") and len(word) > 1:
                    allHashtagsFreq[word] += 1

        allHashtagsFreq = dict(sorted(allHashtagsFreq.items(), key=lambda item: -item[1]))
        return allHashtagsFreq

    def getEmotinalValues(self):
        tweetToEmotionalVal = {}
        for tweet in self.tweets:
            emotionalVal = 0
            words = word_tokenize(tweet['text'])
            for word in words:
                if word in self.wordToEmotion:
                    emotionalVal += int(self.wordToEmotion[word])
            tweetToEmotionalVal[tweet['id']] = emotionalVal

        tweetToEmotionalVal = dict(sorted(tweetToEmotionalVal.items(), key=lambda item: -item[1]))
        return tweetToEmotionalVal

    def saveTweetsEmoVals(self, fileName):
        tweetToEmotionalVal = self.getEmotinalValues()
        tweetToEmotionalValStr = ""
        for tweetId, emoVal in tweetToEmotionalVal.items():
            tweetToEmotionalValStr += f"{tweetId}: {emoVal} \n"
        with open(fileName, "w") as file:
            file.write(tweetToEmotionalValStr)


solution = Solution()

print("\n--- 4.1 ---\n")
hashTagsByFreq = solution.getHashtagsByFreq()
top10 = list(hashTagsByFreq.items())[:10]
print("The most popular hashtags are: ")
for hashtag, freq in top10:
    print(f"- {hashtag} {freq}")

print("\n--- 4.1 ---\n")

print("\n--- 4.2 ---\n")
solution.saveTweetsEmoVals("save.txt")
print("Saved the file!")
print("\n--- 4.2 ---\n")

print("\n--- 4.3 ---\n")
tweetsEmoVals = solution.getEmotinalValues()
tweetsEmoVals = list(tweetsEmoVals.items())
top10MostPos = tweetsEmoVals[:10]
top10MostNeg = tweetsEmoVals[-10:]

print("The most positive tweets are: ")
for tweetId, emoVal in top10MostPos:
    print(f"- {tweetId}: {emoVal}")

print("The most negative tweets are: ")
for tweetId, emoVal in top10MostNeg:
    print(f"- {tweetId}: {emoVal}")
print("\n--- 4.3 ---\n")
