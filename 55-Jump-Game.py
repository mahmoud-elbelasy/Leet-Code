class Solution(object):
    def canJump(self, nums):
        gas = 0
        for i in nums:
            if gas < 0:
                return False
            elif i > gas:
                gas = i
            gas -= 1
        
        return True


        """
        :type nums: List[int]
        :rtype: bool
        """
        