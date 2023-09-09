class Solution(object):
    def twoSum(self, nums, target):
        hashmap = {} #v:n
        
        for val,num in enumerate(nums):
            diff = target - num
            if diff in hashmap:
                return [hashmap[diff], val]
            hashmap[num]  = val
        return
                
        