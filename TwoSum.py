from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        maximum = len(nums)
        dict = {}
        for i in range(maximum):
            diff = target - nums[i]
            if diff in dict:
                return [i, dict[diff]] if i < dict[diff] else [dict[diff], i]
            dict[nums[i]] = i
        return []
            

test = Solution()
print(test.twoSum([1, 2, 4, 6], 10))
