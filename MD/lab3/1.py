from collections import defaultdict

class Solution():
    def canFinish(self, numCourses, prerequisites):
        self.map = defaultdict(list)
        self.visited = set()
        self.visiting = set()

        if len(prerequisites) == 0:
            return True

        for i in range(len(prerequisites)):
            self.map[prerequisites[i][1]].append(prerequisites[i][0])

        for i in range(numCourses):
            if not self.dfs(i):
                return False

        return True

    def dfs(self, val):
        if val in self.visiting:
            return False

        if val in self.visited:
            return True

        self.visiting.add(val)
        for next in self.map[val]:
            if not self.dfs(next):
                return False

        self.visiting.remove(val)
        self.visited.add(val)

        return True


solution = Solution()

print(solution.canFinish(2, [[1,0]]))
print(solution.canFinish(2, [[0,1], [1,0]]))
print(solution.canFinish(5, [[1,4],[2,4],[3,1],[3,2]]))
