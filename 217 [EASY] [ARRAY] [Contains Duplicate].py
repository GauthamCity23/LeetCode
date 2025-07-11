class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        '''
        Idea: 
            1) Store items in a set (removes duplicates)
            2) Compare length of set vs length of array
            3) If lengths aren't the same, that means duplicate found
        '''

        mySet = set(nums)

        return len(mySet) != len(nums)
