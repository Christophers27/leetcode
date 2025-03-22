from collections import deque


class Solution:
    def countCompleteComponents(self, n, edges):
        adjacencyList = [[] for _ in range(n)]
        for u, v in edges:
            adjacencyList[u].append(v)
            adjacencyList[v].append(u)

        visited = [False] * n
        res = 0

        def bfs(node):
            queue = deque([node])
            visited[node] = True
            component = []
            edgeCount = 0

            while queue:
                cur = queue.popleft()
                component.append(cur)
                edgeCount += len(adjacencyList[cur])

                for neighbor in adjacencyList[cur]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        queue.append(neighbor)

            return component, edgeCount // 2

        for i in range(n):
            if not visited[i]:
                component, edgeCount = bfs(i)
                if edgeCount == len(component) * (len(component) - 1) // 2:
                    res += 1

        return res
