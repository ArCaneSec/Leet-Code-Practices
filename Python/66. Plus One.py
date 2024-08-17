class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        current = -1
        last = digits[-1]

        while last == 9:
            digits[current] = 0
            current -= 1
            if len(digits) + current < 0:
                digits.insert(0, 0)
                break
            else:
                last = digits[current]
        
        digits[current] += 1
        return digits

print(Solution().plusOne([9,9,9]))