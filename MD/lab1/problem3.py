from typing import List

class Solution:
    def nextArray(self, arr: List) -> List:
        n = len(arr)
        pivot = None

        for j in range(n - 2, -1, -1): # -1 because it will stop at 0, -1 to decrease the val
            if arr[j] < arr[j + 1]:
                pivot = j
                break

        if pivot is None:
            arr.reverse()
            return arr


        for j in range(n - 1, pivot, -1):
            if arr[j] > arr[pivot]:
                arr[pivot], arr[j] = arr[j], arr[pivot]
                break

        arr[pivot + 1:] = reversed(arr[pivot + 1:]) # + 1 to not include the pivot in the reverse op
        # reverse op done because the of the first loop we know that all the elements on the right of the
        # pivot are in descending order, so we do a reverse op to make them ascending, to make the number as small
        # as possible after doing the swap

        return arr

solution = Solution()
input = input("Input the array separated by spaces: ")
input = input.split(" ")
print(solution.nextArray(input))

# print(solution.nextArray([1]) == [1])
# print(solution.nextArray([3, 2, 1]) == [1, 2, 3])
# print(solution.nextArray([1, 2, 3]) == [1, 3, 2])
# print(solution.nextArray([1, 2]) == [2, 1])
# print(solution.nextArray([2, 1]) == [1, 2])
# print(solution.nextArray([2, 2, 2]) == [2, 2, 2])
# print(solution.nextArray([1, 1, 2]) == [1, 2, 1])
# print(solution.nextArray([1, 3, 2]) == [2, 1, 3])
# print(solution.nextArray([1, 2, 3, 6, 5, 4]) == [1, 2, 4, 3, 5, 6])
# print(solution.nextArray([1, 4, 3, 2]) == [2, 1, 3, 4])
# print(solution.nextArray([1, 5, 8, 4, 7, 6, 5, 3, 1]) == [1, 5, 8, 5, 1, 3, 4, 6, 7])
# print(solution.nextArray([2, 3, 1, 3, 3]) == [2, 3, 3, 1, 3])
# print(solution.nextArray([5, 1, 1, 5, 5]) == [5, 1, 5, 1, 5])


#     Version 1
#     def nextArray(self, arr: List) -> List:
#         max = float('-inf')
#         maxIndex = 0
#         index = 0
#
#         for _ in range(len(arr)):
#             max = float('-inf')
#             maxIndex = 0
#
#             for j in range(index, len(arr)):
#                 if arr[j] > max:
#                     max = arr[j]
#                     maxIndex = j
#
#             if index != maxIndex:
#                 break
#             index += 1
#
#         if maxIndex == len(arr) - 1:
#             arr.reverse()
#             return arr
#
#         arr[maxIndex-1], arr[maxIndex] = arr[maxIndex], arr[maxIndex-1]
#         return arr
