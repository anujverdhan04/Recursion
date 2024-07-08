class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #Using Iteration
        power_set =[[]]
        for element in nums:
            power_set += [subset + [element] for subset in power_set]
        return power_set
'''            
        # Using Recursion
        if not nums:
            return [set()]
        first = nums[0]
        rest = nums[1:]
        without_first = self.subsets(rest)
        with_first = [subset | {first} for subset in without_first]
        return without_first + with_first
'''
        