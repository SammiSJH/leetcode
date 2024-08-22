# 2024-8-22
class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums)


        cache = [nums[0], max(nums[0], nums[1])]

        for i in range(2, len(nums)):
            cache.append(max(cache[i-1], nums[i] + cache[i-2]))

        return cache[-1]