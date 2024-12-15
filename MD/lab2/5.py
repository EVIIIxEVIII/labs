import nltk
from nltk.corpus import words

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def decryptMessage(key, message):
    translated = []

    keyIndex = 0
    key = key.upper()

    for symbol in message:
        num = LETTERS.find(symbol.upper())
        if num != -1:
            num -= LETTERS.find(key[keyIndex])
            num %= len(LETTERS)

            if symbol.isupper():
                translated.append(LETTERS[num])
            elif symbol.islower():
                translated.append(LETTERS[num].lower())

            keyIndex += 1
            if keyIndex == len(key):
                keyIndex = 0
        else:
            translated.append(symbol)

    return ''.join(translated)

def percentageOfEnglishWords(text, words):
    text = text.lower()
    matches = sum(text[i:j] in words for i in range(len(text)) for j in range(i + 1, len(text) + 1))
    total_substrings = (len(text) * (len(text) + 1)) // 2
    return (matches / total_substrings) * 100 if total_substrings > 0 else 0


def hackVigenereDictionary(ciphertext, words):
    for word in words:
        word = word.strip()
        decryptedText = decryptMessage(word, ciphertext)
        if percentageOfEnglishWords(decryptedText, words) > 11:
            print()
            print('Possible encryption break:')
            print('Key ' + str(word) + ': ' + decryptedText[:100])
            print()

nltk.download('words')
words = set(words.words())
ciphertext = """OOGNVMTNTCLUOGZSZSHTXAZGMOMEPKWDDQM"""
hackVigenereDictionary(ciphertext, words)
