import nltk
import json
from collections import defaultdict
from datetime import datetime
import matplotlib.pyplot as plt

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('averaged_perceptron_tagger_eng')

class Solution():
    tweets = []
    punctuation = set(["@", ":", ".", ",", "https", "RT", "..", "*", "%", "’", "/", "[", "]", "http", "``"])
    nonNNP = set(["VR", "CPU"])
    customNNPs = set(["mathowie"])

    def __init__(self):
        self.loadTweets()

    def customTagger(self, words):
        tokens = words.copy()
        customTaggedTokens = []
        for token in words:
            if token in self.nonNNP:
                customTaggedTokens.append((token, "NN"))
                tokens.remove(token)
            if token in self.customNNPs:
                customTaggedTokens.append((token, "NNP"))
                tokens.remove(token)

        return nltk.pos_tag(tokens) + customTaggedTokens

    def getWordsByPopularity(self):
        wordToRetweets = defaultdict(lambda : 0)
        wordToLikes = defaultdict(lambda : 0)

        for tweet in self.tweets:
            words = nltk.tokenize.word_tokenize(tweet['text'])
            pos_tags = self.customTagger(words)
            nouns = [word for word, tag in pos_tags if tag in ("NN", "NNS", "NNPS", "NNP")]
            for noun in nouns:
                if noun in self.punctuation: continue
                wordToRetweets[noun] += tweet['retweets']
                wordToLikes[noun] += tweet['likes']

        wordToScore = defaultdict(lambda : 0.0)
        nounFrequencies, _ = self.countNouns()
        for word, likes in wordToLikes.items():
            wordToScore[word] = nounFrequencies[word] * (1.4 + wordToRetweets[word]) * (1.2 + likes)

        wordToScore = dict(sorted(wordToScore.items(), key = lambda x: -x[1]))
        return wordToScore

    def suggestWords(self, word):
        wordToFrequency = self.countWords()
        suggestions = []

        for tweetWord, freq in wordToFrequency.items():
            if tweetWord.lower().startswith(word.lower()):
                suggestions.append((tweetWord, freq))
            if len(suggestions) == 3: break

        return suggestions

    def autocomplete(self, word):
        nextWordsMap = defaultdict(lambda : 0)

        for tweet in self.tweets:
            words = nltk.tokenize.word_tokenize(tweet['text'])
            for i in range(len(words)):
                if i+1 == len(words) or words[i+1] in self.punctuation: continue
                if words[i] == word :
                    nextWordsMap[words[i + 1]] += 1

        bestAutocomplete = dict(sorted(nextWordsMap.items(), key = lambda x: -x[1]))
        return bestAutocomplete

    def drawMonthFreqDiag(self, word):
        monthsToCount = defaultdict(lambda : 0)
        for tweet in self.tweets:
            words = nltk.tokenize.word_tokenize(tweet['text'])
            for tweetWord in words:
                if tweetWord == word:
                    month = '-'.join(tweet['created_at'].split('-')[:2])
                    monthsToCount[month] += 1

        monthsToCount = dict(sorted(monthsToCount.items(), key = lambda x: datetime.strptime(x[0], "%Y-%m") ))

        months = list(monthsToCount.keys())
        wordCount = list(monthsToCount.values())

        plt.figure(figsize=(10, 6))  # Set the figure size
        plt.bar(months, wordCount)

        plt.xlabel('Dates')
        plt.ylabel('Word frequency')
        plt.title(f"""Bar Chart of the word "{word}" """)

        plt.show()

        return monthsToCount

    def loadTweets(self):
        with open('tweets.json', 'r') as file:
            self.tweets = json.load(file)

    def countNouns(self):
        nounsCount = defaultdict(lambda : 0)
        properNounsCount = defaultdict(lambda : 0)

        for tweet in self.tweets:
            words = nltk.tokenize.word_tokenize(tweet['text'])
            pos_tags = self.customTagger(words)

            nouns = [word for word, tag in pos_tags if tag in ("NN", "NNS", "NNPS", "NNP")]
            properNouns = [word for word, tag in pos_tags if tag in ("NNPS", "NNP")]

            for noun in nouns:
                if noun not in self.punctuation:
                    nounsCount[noun] += 1

            for properNoun in properNouns:
                if properNoun not in self.punctuation:
                    properNounsCount[properNoun] += 1

        nounsCount = dict(sorted(nounsCount.items(), key = lambda x: -x[1]))
        properNounsCount = dict(sorted(properNounsCount.items(), key = lambda x: -x[1]))

        return [nounsCount, properNounsCount]

    def countWords(self):
        wordsCount = defaultdict(lambda : 0)

        for tweet in self.tweets:
            words = nltk.tokenize.word_tokenize(tweet['text'])
            for word in words:
                if word not in self.punctuation:
                    wordsCount[word] += 1

        wordsCount = dict(sorted(wordsCount.items(), key = lambda x: -x[1]))
        return wordsCount

solution = Solution()

print()
print()
print("--- 4.1 ---")
print("--- 4.2 ---")
print("--- 4.3 ---")
print("--- 4.4 ---")
print("--- 4.5 ---")
print("--- 4.6 ---")
print("--- 4.7 ---")
problem = input("Input the problem > ")

match problem:
    case "4.1":
        wordsCount = list(solution.countWords().items())[:10]
        print("Top 10 most used words are: ")
        for word, count in wordsCount:
            print(f"- {word} -> {count}")

    case "4.2":
        nounsCount, _ = solution.countNouns()
        nounsCount = list(nounsCount.items())[:10]
        print("Top 10 most used nouns are: ")
        for noun, count in nounsCount:
            print(f"- {noun} -> {count}")

    case "4.3":
        _, properNounsCount = solution.countNouns()
        properNounsCount = list(properNounsCount.items())[:10]
        print("Top 10 most used proper nouns are: ")
        for n, c in properNounsCount:
            print(f"- {n} -> {c}")

    case "4.4":
        word = input("Input the word for which to draw the diagram > ")
        monthToCount = solution.drawMonthFreqDiag(word)

    case "4.5":
        wordsByPopularity = list(solution.getWordsByPopularity().items())[:10]
        print("Words by popularity: ")
        for word, score in wordsByPopularity:
            print(f"- {word} {score}")

    case "4.6":
        word = input("Suggestions for > ")
        suggestions = solution.suggestWords(word)
        print(f"Suggestions for word {word}: ")
        for suggestion, freq in suggestions:
            print(f"- {suggestion} ({freq})")

    case "4.7":
        autocompleteFor = input("Autocomplete for > ")
        suggestions = solution.autocomplete(autocompleteFor)
        suggestions = list(suggestions.items())[:3]

        print(f"Possible autocomplete for word {autocompleteFor}: ")
        for suggestion, freq in suggestions:
            print(f"- {suggestion} ({freq})")

