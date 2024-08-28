class Solution:
    def isPalindrome(self, x: int) -> bool:
        string_x = str(x)
        counter = 0
        for i in range(len(string_x) - 1, -1, -1):
            if string_x[counter] != string_x[i]:
                return False
            counter+=1
            
        return True


s = Solution().isPalindrome(-121)
print(s)