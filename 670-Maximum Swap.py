# 2024-09-22
class Solution:
    def maximumSwap(self, num: int) -> int:

        nums = [int(i) for i in str(num)]
        maxIdx = N = len(nums)-1
        swapMin = swapMax = 0

        for i in range(N-1, -1, -1):
            if nums[i] > nums[maxIdx]:
                maxIdx = i

            elif nums[i] < nums[maxIdx]:
                swapMin = i
                swapMax = maxIdx

        nums[swapMin], nums[swapMax] = nums[swapMax], nums[swapMin]

        return int(''.join([str(x) for x in nums]))