class Solution:
    def isMatch(self, string, pattern):
        ...
    
    def backtrack(string, pattern, s, p):
        if string[s] == pattern[p] or pattern[p] == ".":
            ...
        if pattern[p+1] == "*":
            p += 2

print(Solution().isMatch("aa", "a"))