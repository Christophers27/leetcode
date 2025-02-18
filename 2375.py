class Solution:
    def smallestNumber(self, pattern):
        res, stack = [], []

        for num, c in enumerate(pattern + "I", 1):
            stack.append(str(num))

            if c == "I":
                res += stack[::-1]
                stack.clear()

        return "".join(res)
