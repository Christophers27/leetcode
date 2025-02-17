class Solution:
    def numTilePossibilities(self, tiles):
        res = set()

        def dfs(cur, tilesLeft):
            if cur not in res:
                if cur:
                    res.add(cur)
                for i in range(len(tilesLeft)):
                    dfs(cur + tilesLeft[i], tilesLeft[:i] + tilesLeft[i+1:])
        
        dfs("", tiles)
        return len(res)