from collections import defaultdict

class Solution():
    def strongPasswordChecker(self, passwd):
        replacements = self.hasLowerCase(passwd) + self.hasUpperCase(passwd) + self.hasNumerical(passwd)

        inserts = max(0, 6 - len(passwd))
        deletes = max(0, len(passwd) - 20)

        [repeatingGroups, edgeElements] = self.repeatingCharacters(passwd)
        [consecutiveGroups, consCharToGr] = self.consecutiveCharacters(passwd)

        self.repeatingGroups = repeatingGroups
        self.consecutiveGroups = consecutiveGroups

        self.bestDelete(deletes, edgeElements, consCharToGr)
        overlappingSteps = self.overlapHandling(edgeElements, consCharToGr)

        repGroupRep = 0
        for i in range(len(self.repeatingGroups)):
            repGroupRep += self.repeatingGroups[i] // 3

        consGroupRep = 0
        for i in range(len(self.consecutiveGroups)):
            consGroupRep += self.consecutiveGroups[i] // 2

        res = deletes + max(replacements, inserts, consGroupRep + repGroupRep + overlappingSteps)
        return res if res != 0 else "good"

    def hasLowerCase(self, passwd):
        return 1 if not any(c.islower() for c in passwd) else 0

    def hasUpperCase(self, passwd):
        return 1 if not any(c.isupper() for c in passwd) else 0

    def hasNumerical(self, passwd):
        return 1 if not any(c.isdigit() for c in passwd) else 0

    def hasSpecial(self, passwd):
        return 1 if not any(not c.isalnum() for c in passwd) else 0

    def consecutiveCharacters(self, passwd):
        res = []
        currentLength = 0
        prevChar = None

        for i in range(len(passwd)):
            char = passwd[i]

            if prevChar is None:
                currentLength = 1
            elif ord(char) == ord(prevChar) + 1:
                currentLength += 1
            else:
                if currentLength > 0:
                    res.append(currentLength)
                currentLength = 1

            prevChar = char

        if currentLength > 0:
            res.append(currentLength)

        charToGroup = {}
        currentIndex = 0
        for groupID, groupSize in enumerate(res):
            for j in range(groupSize):
                charToGroup[currentIndex + j] = groupID
            currentIndex += groupSize

        return [res, charToGroup]

    def overlapHandling(self, edgeElements, consCharsGroups):
        numSteps = 0
        for groupId, edges in edgeElements.items():
            [start, end] = edges

            if (
                (self.consecutiveGroups[consCharsGroups[start]] == 2)
                and
                (self.consecutiveGroups[consCharsGroups[end]] == 2)
               ):
                if (self.repeatingGroups[groupId] % 3 == 0): # from abbbc -> aXbbX
                    self.repeatingGroups[groupId] -= 1
                    self.repeatingGroups[groupId + 1] -= 1

                    self.consecutiveGroups[consCharsGroups[start]] -= 1
                    self.consecutiveGroups[consCharsGroups[end + 1]] -= 1
                    numSteps += 2

                elif (self.repeatingGroups[groupId] % 3 == 1): # from aaabbbbccc -> aaaXbbXccc
                    self.repeatingGroups[groupId] -= 2

                    self.consecutiveGroups[consCharsGroups[start]] -= 1
                    self.consecutiveGroups[consCharsGroups[end]] -= 1
                    numSteps += 2

                elif (self.repeatingGroups[groupId] % 3 == 2): # from aaabbbbccc -> aaXbbbbbXcc
                    self.repeatingGroups[groupId - 1] -= 1
                    self.repeatingGroups[groupId + 1] -= 1

                    self.consecutiveGroups[consCharsGroups[start - 1]] -= 1
                    self.consecutiveGroups[consCharsGroups[end + 1]] -= 1
                    numSteps += 2

        return numSteps

    def bestDelete(self, deletes, edgeElements, consCharToGr):
        allEdges = []
        for gr, [start, end] in edgeElements.items():
            allEdges.append(start)
            allEdges.append(end)

        for _ in range(deletes):
            repArgmin, repGroupValue = min(
                enumerate(self.repeatingGroups),
                key=lambda it: it[1] % 3 if it[1] >= 3 else float('inf'),
                default=(None, float('inf'))
            )

            consArgmin = None
            for el, gr in consCharToGr.items():
                if (self.consecutiveGroups[gr] < 2) or (el in allEdges):
                    continue
                consArgmin = gr


            if repGroupValue % 3 == 0:
                self.repeatingGroups[repArgmin] -= 1
            elif consArgmin is not None:
                self.consecutiveGroups[consArgmin] -= 1
            else:
                self.repeatingGroups[repArgmin] -= 1

    def repeatingCharacters(self, passwd):
        res = []
        edgeElements = defaultdict(list)
        currentChar = ""

        for i in range(len(passwd)):
            if passwd[i] != currentChar:
                res.append(1)
                currentChar= passwd[i]
            else:
                res[-1] += 1

        for i in range(len(res)):
            if res[i] >= 3:
                start = sum(res[:i])
                end = start + res[i] - 1

                edgeElements[i].append(start)
                edgeElements[i].append(end)

        return [res, edgeElements]


    def checkLen(self, passwd, minlen, maxlen, added):
        passWithAddedLen = len(passwd) + added
        passLen = len(passwd)

        if passWithAddedLen >= minlen and passWithAddedLen <= maxlen:
            return 0

        if passWithAddedLen < minlen:
            return minlen - passWithAddedLen

        if passWithAddedLen > maxlen:
            return passLen - maxlen

        return 0


passwordChecker = Solution()
# print("Aa1!bZ9@", passwordChecker.strongPasswordChecker("Aa1!bZ9@") == "good", "good", passwordChecker.strongPasswordChecker("Aa1!bZ9@"))
# print("abbbcc-0", passwordChecker.strongPasswordChecker("abbbcc-0") == 1, 1, passwordChecker.strongPasswordChecker("abbbcc-0"))
# print("abcbbcc-0", passwordChecker.strongPasswordChecker("abcbbcc-0") == "good", "good", passwordChecker.strongPasswordChecker("abcbbcc-0"))
# print("A!b1!A!b1!", passwordChecker.strongPasswordChecker("A!b1!A!b1!") == "good", "good", passwordChecker.strongPasswordChecker("A!b1!A!b1!"))
# print("12345678", passwordChecker.strongPasswordChecker("12345678") == 5, 5, passwordChecker.strongPasswordChecker("12345678"))
# print("Abcdefgh", passwordChecker.strongPasswordChecker("Abcdefgh") == 2, 2, passwordChecker.strongPasswordChecker("Abcdefgh"))
# print("Zz1?", passwordChecker.strongPasswordChecker("Zz1?") == 4, 4, passwordChecker.strongPasswordChecker("Zz1?"))
print("b1111", passwordChecker.strongPasswordChecker("b1111") == 1, 1, passwordChecker.strongPasswordChecker("b1111"))
print("aaa111", passwordChecker.strongPasswordChecker("aaa111") == 2, 2, passwordChecker.strongPasswordChecker("aaa111"))
print("aaaB1", passwordChecker.strongPasswordChecker("aaaB1") == 1, 1, passwordChecker.strongPasswordChecker("aaaB1"))
print("a", passwordChecker.strongPasswordChecker("a") == 5, 5, passwordChecker.strongPasswordChecker("a"))
print("ABABABABABABABABABAB1", passwordChecker.strongPasswordChecker("ABABABABABABABABABAB1") == 2, 2, passwordChecker.strongPasswordChecker("ABABABABABABABABABAB1"))
print("bbaaaaaaaaaaaaaaacccccc", passwordChecker.strongPasswordChecker("bbaaaaaaaaaaaaaaacccccc") == 8, 8, passwordChecker.strongPasswordChecker("bbaaaaaaaaaaaaaaacccccc"))
print("FFFFFFFFFFFFFFF11111111111111111111AAA", passwordChecker.strongPasswordChecker("FFFFFFFFFFFFFFF11111111111111111111AAA") == 23, 23, passwordChecker.strongPasswordChecker("FFFFFFFFFFFFFFF11111111111111111111AAA"))
print("A1234567890aaabbbbccccc", passwordChecker.strongPasswordChecker("A1234567890aaabbbbccccc"))
print("aaabbbccc", passwordChecker.strongPasswordChecker("aaabbbccc"))
print("aaabbbbbcccc", passwordChecker.strongPasswordChecker("aaabbbbbcccc"))
print("aaE-d2c1", passwordChecker.strongPasswordChecker("aaE-d2c1"))
