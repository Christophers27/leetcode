class Solution:
    def countOfSubstrings(self, word, k):
        N = len(word)
        res = 0
        vowels = set('aeiou')

        nextConsonant = [N] * N
        index = N
        for i in range(N-1, -1, -1):
            nextConsonant[i] = index
            if word[i] not in vowels:
                index = i
        
        vowelCount = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}
        consonantCount = 0
        left = 0

        for right in range(N):
            c = word[right]
            if c in vowels:
                vowelCount[c] += 1
            else:
                consonantCount += 1
            
            while consonantCount > k and left <= right:
                leftC = word[left]
                if leftC in vowels:
                    vowelCount[leftC] -= 1
                else:
                    consonantCount -= 1
                left += 1
            
            while left <= right and consonantCount == k and all(vowelCount[c] >= 1 for c in vowels):
                res += nextConsonant[right] - right
                leftC = word[left]
                if leftC in vowels:
                    vowelCount[leftC] -= 1
                else:
                    consonantCount -= 1
                left += 1
        
        return res
    