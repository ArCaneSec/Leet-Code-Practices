class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i =  m - 1
        j = n - 1
        k = m + n - 1

        for _ in nums1[::-1]:
            if j < 0:
                return
            elif i < 0:
                nums1[k] = nums2[j]
                j -= 1
            
            elif nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            
            k -= 1

test = [2,0]
test2 = [1]
Solution().merge(test, 1, test2, 1)
print(test)
