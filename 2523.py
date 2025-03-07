class Solution:
    def closestPrimes(self, left, right):
        primes = set([i for i in range(2, right + 1)])

        for i in range(2, int(right ** 0.5) + 1):
            if i in primes:
                for j in range(2 * i, right + 1, i):
                    if j in primes:
                        primes.remove(j)
        
        primes = sorted(list(primes))
        res = []
        minDiff = float('inf')

        for i in range(1, len(primes)):
            diff = primes[i] - primes[i - 1]
            if diff < minDiff and primes[i - 1] >= left and primes[i] <= right:
                minDiff = diff
                res = [primes[i - 1], primes[i]]
        
        return res if res else [-1, -1]
        
