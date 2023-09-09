class Solution(object):
    def twoSum(self, nums, target):
        result = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j :
                    if nums[i] + nums[j] == target:
                        if i and j not in result:
                            result.append(i)
                            result.append(j)
        return result
                    
        