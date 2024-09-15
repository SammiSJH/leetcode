# 2024-09-14
class SparseVector:
    def __init__(self, nums: List[int]):

        self.numsDict = {}
        for i, num in enumerate(nums):
            if num != 0:
                self.numsDict[i] = num

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:

        res = 0
        for key, val in self.numsDict.items():
            if key in vec.numsDict.keys():
                res += self.numsDict[key] * vec.numsDict[key]

        return res