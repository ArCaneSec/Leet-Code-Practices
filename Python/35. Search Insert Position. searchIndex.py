class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        low = 0
        mid = int(len(nums) / 2)
        high = len(nums) - 1

        while low <= high:
            mid = int((low + high) / 2)

            half = nums[mid]
            if target > half:
                low = mid + 1
            elif target < half:
                high = mid - 1
            elif target == half:
                return mid
            
        return low