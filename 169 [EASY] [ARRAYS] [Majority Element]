class Solution:
    def majorityElement(self, nums: List[int]) -> int: 

        '''
        Steps:
        1) set r to first number, counter to 0
        2) if we ever go negative, reset c->1 and r-> current number
        3) This works, cause if we ever go negative, that means we have a new canidate
            --> Because negative means not majority
        4) Return Final r value
        '''

        r = nums[0]
        c = 0

        for num in nums:
            if num == r:
                c = c + 1
            else:
                c = c - 1
            
            if c == 0:
                r = num
                c = 1
        return r

        '''
        Steps

        1) Store counts in Dict
        2) Once u have more than 0/5

        d = {}
        half = len(nums)//2
        for num in nums:
            if num not in d:
                d[num] = 1
            else:
                d[num] = d[num] + 1
                if d[num] > half:
                    return num
        return nums[0]
        '''