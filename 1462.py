from collections import defaultdict

class Solution:
    def checkIfPrerequisite(self, N, prerequisites, queries):
        postreqs = defaultdict(list)
        for prereq, postreq in prerequisites:
            postreqs[prereq].append(postreq)
        
        reqs = [set() for _ in range(N)]

        def dfs(course):
            for postreq in postreqs[course]:
                if postreq not in reqs[course]:
                    reqs[course].add(postreq)
                    reqs[course].update(dfs(postreq))
            
            return reqs[course]
        
        for i in range(N):
            dfs(i)
        
        res = []
        for prereq, postreq in queries:
            if postreq not in reqs[prereq]:
                res.append(False)
            else:
                res.append(True)
        
        return res