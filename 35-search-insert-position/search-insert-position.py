class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            if target == nums[0]:
                return 0
        size = len(nums) - 1
        if not target in nums:
            if target > nums[size]:
                return size + 1
            elif target < nums[0]:
                return 0
            else:
                for i in range(size+1):
                    if nums[i] >= target:
                        return i
        else:
            for i in range(size+1):
                if target == nums[i]:
                    return i