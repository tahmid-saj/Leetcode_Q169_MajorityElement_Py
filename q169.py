class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        # 1 1 1 2 2 2 2
        # currNum = nums[0], countNum = 0
        # loop through nums using i:
        # if currNum != nums[i]: currNum = nums[i], countNum = 1
        # else: countNum += 1
        # if countNum >= n // 2: return currNum
        # return currNum
        if len(nums) == 1: return nums[0]

        currNum, countNum = nums[0], 0
        for i in range(0, len(nums)):
            if currNum != nums[i]:
                currNum = nums[i]
                countNum = 1
            else:
                countNum += 1

            if countNum > len(nums) // 2: return currNum

        return currNum
