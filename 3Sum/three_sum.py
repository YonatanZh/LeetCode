TARGET = 0
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        j = 0
        k = 0
        unique_tirplets = set()

        for i in range(len(nums) - 2):
            if nums[i] > TARGET:
                break
            j = i + 1
            k = len(nums) - 1
            while (j < k):
                sum = nums[i] + nums[j] + nums[k]
                if sum == TARGET:
                    triplet = (nums[i], nums[j], nums[k])
                    if triplet not in unique_tirplets:
                        unique_tirplets.add((triplet))
                    j += 1
                    k -= 1
                elif sum < TARGET:
                    j += 1
                else:
                    k -= 1

        return list(unique_tirplets)
