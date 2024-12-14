class Solution:
    def xnor(self, val1: bool|int, val2: bool|int) -> bool:
        x1 = bool(val1)
        x2 = bool(val2)
        return (x1 and x2) or (not x1 and not x2)

solution = Solution()

input1 = input("Input value 1: ")
input2 = input("Input value 2: ")

print(solution.xnor(bool(input1), bool(input2)))
