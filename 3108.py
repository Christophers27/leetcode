class Solution:
    def minimumCost(self, n, edges, queries):
        parent = list(range(n))
        minCost = [-1] * n
        res = []

        def findRoot(x):
            if parent[x] != x:
                parent[x] = findRoot(parent[x])
            return parent[x]

        for left, right, weight in edges:
            leftRoot = findRoot(left)
            rightRoot = findRoot(right)

            minCost[rightRoot] &= weight

            if leftRoot != rightRoot:
                minCost[rightRoot] &= minCost[leftRoot]
                parent[leftRoot] = rightRoot

        for left, right in queries:
            if left == right:
                res.append(0)
            elif findRoot(left) != findRoot(right):
                res.append(-1)
            else:
                res.append(minCost[findRoot(left)])

        return res
