# class Solution(object):
    # def threeSum(self, nums):
    #     value=nums
    #     for i in range(nums):
    #         if nums[i]<=2:
    #             nums=nums[0]+nums[1]+ nums[2]
    #         elif i<=0:
    #             return nums
    #         else:
    #             nums=nums+1
    #         for i in range(nums):
    #             for j in range(nums):
    #                 for k in range(nums):
    #                     if i!=j or i!=k or j!=k or nums[i]+num[j]+nums[k]== 0:
    #                         return nums
    #                     else:
    #                         return nums+1
class Solution:
    def threeSum(self, nums):
        nums.sort()
        n = len(nums)
        res = []

        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, n - 1
            while left < right:
                s = nums[i] + nums[left] + nums[right]
                if s == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif s < 0:
                    left += 1
                else:
                    right -= 1

        return res
    
        