class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash = {}
        for index, num in enumerate(nums):
            complement = target - num
            if complement in num_dict:
                return [hash[complement], index]
            hash[num] = index
