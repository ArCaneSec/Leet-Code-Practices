class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        max_len = len(word1) + len(word2)
        complete_word = ""
        word1_len = len(word1)
        word2_len = len(word2)

        for i in range(0, max_len):
            if word1_len - 1 >= i:
                complete_word += word1[i]

            if word2_len -1 >= i:    
                complete_word += word2[i]
        print(complete_word)
        return complete_word

Solution().mergeAlternately("test", "newtest")