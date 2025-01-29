from collections import defaultdict

class Solution:
    def findRedundantConnection(self, edges):
        graph = defaultdict(list)  # Adjacency list
        visited = defaultdict(bool)  # Visited nodes

        def wasConnected(u, v):
            if u == v:
                return True

            for neighbour in graph[u]:
                if not visited[neighbour]:
                    visited[neighbour] = True
                    if wasConnected(neighbour, v):
                        return True
            
            return False

        for u, v in edges:
            if wasConnected(u, v):
                return [u, v]
            
            graph[u].append(v)
            graph[v].append(u)

            visited = defaultdict(bool)
            
