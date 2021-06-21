
link: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/ 

# # Solution A: hashmap
# class Solution:
#     def twoSum(self, numbers: List[int], target: int) -> List[int]:
#         hashmap = {}
#         for i in range(len(numbers)):
#             if target - numbers[i] in hashmap:
#                 return [hashmap[target - numbers[i]] + 1, i + 1]
#             hashmap[numbers[i]] = i
            
            
# Solution B: Binary search
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            left = i
            right = len(numbers)
            while left < right:
                mid = (left + right) // 2
                if numbers[mid] > target:
                    right = mid
                elif numbers[mid] < target:
                    left = mid
            if numbers[left] + numbers[right] == target:
                return [left + 1, right + 1]
