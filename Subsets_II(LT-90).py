class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # Sort the numbers to handle duplicates easily
        power_set = [[]]
        
        for element in nums:
            # Create new subsets from the current element and existing subsets
            new_subsets = []
            for subset in power_set:
                new_subset = subset + [element]
                new_subsets.append(new_subset)
            power_set.extend(new_subsets)
        unique_subsets = set(tuple(subset) for subset in power_set)    
        return [list(subset) for subset in unique_subsets]   

