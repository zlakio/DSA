class Solution(object):
    def myPow(self, x, n):
        self.x = x
        self.n = n
        x: float
        n: int
        if x == 0 or n < 0:
            return
        if x in range(-99, 100):
            return x**n


s = Solution()
print(s.myPow(2, 4))
