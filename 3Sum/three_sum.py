TARGET = 0
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        l = 0
        r = 0
        unique_tirplets = set()

        for i in range(len(nums) - 2):
            if nums[i] > TARGET:
                break
            l = i + 1
            r = len(nums) - 1
            while (l < r):
                sum = nums[i] + nums[l] + nums[r]
                if sum == TARGET:
                    triplet = (nums[i], nums[l], nums[r])
                    if triplet not in unique_tirplets:
                        unique_tirplets.add((triplet))
                    l += 1
                    r -= 1
                elif sum < TARGET:
                    l += 1
                else:
                    r -= 1

        return list(unique_tirplets)
