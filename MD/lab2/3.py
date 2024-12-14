class Solution():
    def strongPasswordChecker(self, passwd):
        replacements = self.hasLowerCase(passwd) + self.hasUpperCase(passwd) + self.hasNumerical(passwd)

        inserts = max(0, 6 - len(passwd))
        deletes = max(0, len(passwd) - 20)

        repeatingChars = self.repeatingCharacters(passwd)
        consecutiveChars = self.consecutiveChars(passwd)

        self.bestDelete(deletes, repeatingChars, consecutiveChars)

        repGroupRep = 0
        for i in range(len(repeatingChars)):
            repGroupRep += repeatingChars[i] // 3

        consGroupRep = 0
        for i in range(len(consecutiveChars)):
            consGroupRep += consecutiveChars[i] // 2

        print(consecutiveChars)
        print("consGroupRep :", consGroupRep)
        print("repGroupRep: ", repGroupRep)

        return deletes + max(replacements, repGroupRep + consGroupRep, inserts)

    def hasLowerCase(self, passwd):
        return 1 if not any(c.islower() for c in passwd) else 0

    def hasUpperCase(self, passwd):
        return 1 if not any(c.isupper() for c in passwd) else 0

    def hasNumerical(self, passwd):
        return 1 if not any(c.isdigit() for c in passwd) else 0

    def hasSpecial(self, passwd):
        return 1 if not any(not c.isalnum() for c in passwd) else 0

    def consecutiveChars(self, passwd):
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

        return res

    def bestDelete(self, deletes, repeatingGroups, consecutiveGroups):
        for _ in range(deletes):
            repArgmin, repGroupValue = min(
                enumerate(repeatingGroups),
                key=lambda it: it[1] % 3 if it[1] >= 3 else float('inf'),
                default=(None, float('inf'))
            )

            consArgmin, consGroupValue = min(
                enumerate(consecutiveGroups),
                key=lambda it: it[1] % 2 if it[1] >= 2 else float('inf'),
                default=(None, float('inf'))
            )

            # TODO: avoid removing consecutive chars at the edges of repeted chars
            if repGroupValue % 3 == 0:
                repeatingGroups[repArgmin] -= 1 # substrings like aaa require 1 delete to avoid 1 insert
            elif consGroupValue % 2 == 0:
                consecutiveGroups[consArgmin] -= 1 # 12 require 1 delete to avoid 1 insert

            elif repGroupValue % 2 == 0: # substrings like aaaaa require 2 deletes to avoid 1 insert
                repeatingGroups[repArgmin] -= 1
            elif consGroupValue % 1 == 0:
                consecutiveGroups[consArgmin] -= 1

            else:
                repeatingGroups[repArgmin] -= 1 # deleting substrings like aaaaaaaa
                # is very ineficient because it would requre 3 deletes to avoid 1 insert

    def repeatingCharacters(self, passwd):
        res = []
        currentChar = ""

        for i in range(len(passwd)):
            if passwd[i] != currentChar:
                res.append(1)
                currentChar= passwd[i]
            else:
                res[len(res) - 1] += 1

        return res


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
# print("1337C0d3", passwordChecker.strongPasswordChecker("a1337C0d3") == "good", "good", passwordChecker.strongPasswordChecker("a1337C0d3"))
print("b1111", passwordChecker.strongPasswordChecker("b1111") == 1, 1, passwordChecker.strongPasswordChecker("b1111"))
print("aaa111", passwordChecker.strongPasswordChecker("aaa111") == 2, 2, passwordChecker.strongPasswordChecker("aaa111"))
print("aaaB1", passwordChecker.strongPasswordChecker("aaaB1") == 1, 1, passwordChecker.strongPasswordChecker("aaaB1"))
print("a", passwordChecker.strongPasswordChecker("a") == 5, 5, passwordChecker.strongPasswordChecker("a"))
print("ABABABABABABABABABAB1", passwordChecker.strongPasswordChecker("ABABABABABABABABABAB1") == 2, 2, passwordChecker.strongPasswordChecker("ABABABABABABABABABAB1"))
print("bbaaaaaaaaaaaaaaacccccc", passwordChecker.strongPasswordChecker("bbaaaaaaaaaaaaaaacccccc") == 8, 8, passwordChecker.strongPasswordChecker("bbaaaaaaaaaaaaaaacccccc"))
print("FFFFFFFFFFFFFFF11111111111111111111AAA", passwordChecker.strongPasswordChecker("FFFFFFFFFFFFFFF11111111111111111111AAA") == 23, 23, passwordChecker.strongPasswordChecker("FFFFFFFFFFFFFFF11111111111111111111AAA"))
print("A1234567890aaabbbbccccc", passwordChecker.strongPasswordChecker("A1234567890aaabbbbccccc") == 4, 4, passwordChecker.strongPasswordChecker("A1234567890aaabbbbccccc"))
