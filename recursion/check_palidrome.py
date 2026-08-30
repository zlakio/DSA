"""def f(i, n, l):
    if i >= n / 2:
        return True
    if l[i] != l[n - i - 1]:
        return False
    return f(i + 1, n, l)


l = "aya"
print(f(0, len(l), l))"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        c = ""
        for i in s:
            if i.isalnum():  # removes spaces because isalnum returns False for space and other special characters , and therefore clean has only al and nums
                c += i.lower()

        def help(i):
            n = len(c)
            if i >= (n * 0.5):
                return True
            if c[i] != c[n - i - 1]:
                return False
            return help(i + 1)

        return help(0)


s = Solution()
print(s.isPalindrome("race car"))
