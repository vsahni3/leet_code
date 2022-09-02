# def three_sum(nums):
#     combos = set()
#     num_map = {nums[i] : i for i in range(len(nums))}
#     print(num_map)
#     for i in range(len(nums) - 2):
#         for j in range(i+1, len(nums) - 1):
#             sum = nums[i] + nums[j]
#             search_for = -1 * sum
#             if search_for in num_map:
#                 index = num_map[search_for]
#                 if index > j:
#                     combos.add(tuple(sorted([nums[i], nums[j], search_for])))
#                     continue
#     return list(combos)
# print(three_sum([0, 0, 0]))

def three_sum(nums):
    combos = set()
    num_map = {}
    for i in range(len(nums)):
        if nums[i] not in num_map:
            num_map[nums[i]] = i
    # print(num_map)
    for i in range(len(nums) - 1):
        for j in range(i+1, len(nums)):
            sum = nums[i] + nums[j]
            search_for = -1 * sum
            if search_for in num_map:
                index = num_map[search_for]
                if i != index != j:
                    combos.add(tuple(sorted([nums[i], nums[j], search_for])))
                    continue
    return list(combos)
print(three_sum([0]))


