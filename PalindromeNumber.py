class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        reversed = int(str(x)[::-1])
        if x == reversed:
            return True
        return False
    
test = Solution()
x = test.isPalindrome(1233121)
print(x)