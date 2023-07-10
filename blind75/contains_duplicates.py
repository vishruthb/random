class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        num_set = set() # use set for efficient lookup
        for num in nums:
            if num in num_set:
                return True
            num_set.add(num)
        return False

if __name__ == "__main__":
    solution = Solution()
    
    nums1 = [2,14,18,22,22]
    print(solution.containsDuplicate(nums1))
