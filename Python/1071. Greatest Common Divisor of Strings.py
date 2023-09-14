class Solution:

    def cut_to_half(self, str1, str2):
        middle = len(str2) / 2
        middle = int(middle)
        print(middle)
        middle_chars = str2[:middle]
        print(middle_chars)
        if middle_chars in str1:
            self.cut_to_half(str1, middle_chars)
        else:
            return middle_chars

    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str2 in str1:
            test = self.cut_to_half(str1, str2)
            print(test)


Solution().gcdOfStrings("abab", "ab")