# class Solution:
#     def threeSumClosest(self, nums: List[int], target: int) -> int:
#         def binary_search(sublist, search_for):
#             index = len(sublist) // 2
#             while len(sublist) > 1:

#                 if sublist[index-1] <= search_for <= sublist[index] or len(sublist) == 2:
#                     diff1 = abs(sublist[index-1] - search_for)
#                     diff2 = abs(sublist[index] - search_for)
#                     if diff1 < diff2:
#                         return sublist[index-1]
#                     else:
#                         return sublist[index]


#                 if sublist[index] < search_for:
#                     sublist = sublist[index:]
#                 elif sublist[index] == search_for:
#                     return sublist[index]

#                 else:
#                     sublist = sublist[:index]
#                 index = len(sublist) // 2

#             return sublist[0]

#         nums.sort()
#         best = 10 ** 7
#         for i in range(len(nums) - 2):
#             for j in range(i+1, len(nums) - 1):
#                 cur = nums[i] + nums[j]
#                 search_for = target - cur
#                 print(search_for, cur)
#                 sublist = nums[j+1:]
#                 closest_num = binary_search(sublist, search_for)
#                 final = cur + closest_num
#                 if abs(final - target) < abs(best - target):
#                     best = final
#         return best    

def closest(nums, target):
    best = 10 ** 7
    for i in range(len(nums) - 2):
        for j in range(i+1, len(nums) - 1):
            for k in range(j + 1, len(nums)):
                result = nums[i] + nums[j] + nums[k]
                if abs(target - result) < abs(target - best):
                    best = result 
    return best
print(closest([-1,2,1,-4], 1))