class Solution:
    def eventualSafeNodes(self, graph):
        N = len(graph)
        visited, inStack = [False] * N, [False] * N

        for i in range(N):
            self.inLoop(i, graph, visited, inStack)

        res = []
        for i in range(N):
            if not inStack[i]:
                res.append(i)

        return res

    def inLoop(self, node, graph, visited, inStack):
        if inStack[node]:
            return True  # This was called in a loop-checker so its a loop
        if visited[node]:
            return False  # We already checked this node before

        visited[node] = True
        inStack[node] = True

        for neighbour in graph[node]:
            if self.inLoop(neighbour, graph, visited, inStack):
                return True

        inStack[node] = False
        return False
