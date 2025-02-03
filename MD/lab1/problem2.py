class Solution:
    def xnor(self, val1: bool|int, val2: bool|int) -> bool:
        x1 = bool(val1)
        x2 = bool(val2)
        return (x1 and x2) or (not x1 and not x2)

solution = Solution()

print("Values: true, false, 1, 0")
input1 = input("Input value 1: ")
input2 = input("Input value 2: ")

map = {
    "true": 1,
    "True": 1,
    "false": 0,
    "False": 0,
    1: 1,
    0: 0
}

print(solution.xnor(bool(map[input1]), bool(map[input2])))
