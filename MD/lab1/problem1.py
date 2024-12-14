from typing import List

class Solution:
    def getPowerset(self, set: List) -> List:
        n = len(set)
        ans = []

        for i in range(2**n):
            # indices = "{0:b}".format(i).zfill(len(set))
            tempAns = []

            for j in range(n):
                if i & (1 << j): # check if the jth bit is set to 1 by adding j zeros after the 1.
                    tempAns.append(set[j])

            ans.append(tempAns)

        return ans;


solution = Solution()

input = input("Enter items separated by spaces: ")
input = input.split(" ")

powerset = solution.getPowerset(input);
print("Powerset len: ", len(powerset))
print(powerset)

# let n = 5 => n = 0101
#

# Version 1
#   def getPowerset(self, set: List) -> List:
#       n = len(set)
#       ans = []
#
#       for i in range(2**n):
#           indices = "{0:b}".format(i).zfill(len(set))
#           tempAns = []
#
#           for j in range(n):
#               if indices[j] == "1":
#                   tempAns.append(set[j])
#
#           ans.append(tempAns)
#
#       return ans;
#
