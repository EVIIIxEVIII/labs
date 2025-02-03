class Solution:
    def shortestPalindrome(self, s):
        if s == s[::-1]:
            return s

        lp = 0
        rp = len(s) - 1

        substrPalEnd = rp
        resetTo = 0

        while lp < rp:
            print(lp, rp)
            if s[lp] != s[rp]:
                while s[rp] != s[lp] and rp > lp:
                    rp -= 1

                g = s[rp:rp+lp+1]
                g = g[::-1]

                if s[:lp+1] == g:
                    substrPalEnd = rp + lp
                else:
                    rp = substrPalEnd - 1
                    substrPalEnd -= 1
                    lp = resetTo
            else:
                lp += 1
                rp -= 1

        frontPart = s[substrPalEnd+1:]
        frontPart = frontPart[::-1] # this reverses the string

        return frontPart + s

solution = Solution()

theString = input("Please input the string > ")
print(solution.shortestPalindrome(theString))

