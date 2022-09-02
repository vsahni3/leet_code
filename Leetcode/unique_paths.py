# big = []
# def unique_paths(m, n, cur=[], first=0, second=0):
#     if [first, second] == [m-1, n-1]:
#         big.append(cur)
#     if first < m - 1:
#         unique_paths(m, n, cur+['R'], first+1, second)
#     if second < n - 1:
#         unique_paths(m, n, cur+['D'], first, second+1)
#     return big
# print(unique_paths(3, 2))

# big = []
# def unique_paths(m, n, cur=[], first=0, second=0):
#     if [first, second] == [m-1, n-1]:
#         return cur
#     paths1 = []
#     paths2 = []
#     if first < m - 1:
#         paths1 = unique_paths(m, n, cur+['R'], first+1, second)
#     if second < n - 1:
#         paths2 = unique_paths(m, n, cur+['D'], first, second+1)
    
#     if paths1 != [] and paths2 != []:
#         return paths1 + [' '] +  paths2
#     return paths1 + paths2
# print(unique_paths(3, 3))

# cache = {}

# def unique_paths(m, n, cur=[], first=0, second=0):
#     if [first, second] == [m-1, n-1]:
#         return cur
#     paths1 = []
#     paths2 = []

#     def calc_paths(index1, index2, direction):
#         if (index1, index2) not in cache:
#             cache[(index1, index2)] = unique_paths(m, n, cur + [direction], index1, index2)
#         new = []
#         counter = 0
#         for i in cache[(index1, index2)]:
#             if i != ' ' and counter >= index1 + index2:
#                 new.append(i)
#                 counter += 1
#             else:
#                 new.extend([' '] + cur)
#                 counter = 0
            
#         return new
#     if first < m - 1:
#         if (first+1, second) not in cache:
#             cache[(first+1, second)] = unique_paths(m, n, cur + ['R'], first+1, second)
#         paths1 = cache[(first+1, second)]

#     if second < n - 1:
#         if (first, second+1) not in cache:
#             cache[(first, second+1)] = unique_paths(m, n, cur + ['R'], first, second+1)
#         paths1 = cache[(first, second+1)]

    
#     if paths1 != [] and paths2 != []:
#         return paths1 + [' '] +  paths2
#     return paths1 + paths2
# print(unique_paths(3, 3))

# cache = {}
# def unique_paths(m, n, first=0, second=0):
#     if [first, second] == [m-1, n-1]:
#         return 1
#     paths1 = paths2 = 0
#     def calc_paths(index1, index2):
#         if (index1, index2) not in cache:
#             cache[(index1, index2)] = unique_paths(m, n, index1, index2)

#         return cache[(index1, index2)]
#     if first < m - 1:
#         paths1 = calc_paths(first+1, second)

#     if second < n - 1:
#         paths2 = calc_paths(first, second+1)


#     return paths1 + paths2
# print(unique_paths(100, 100))

# def unique_paths(m, n, cur=[], first=0, second=0):
#     if [first, second] == [m-1, n-1]:
#         return [cur[-1]]
#     paths1 = []
#     paths2 = []
#     if first < m - 1:
#         res =  unique_paths(m, n, cur+['R'], first+1, second)
#         # print(res)
#         paths1 = cur[first + second - 1:] + res
#         # print(paths1)
#     if second < n - 1:
#         res =  unique_paths(m, n, cur+['D'], first, second+1)
#         # print(res)
#         paths2 = cur[first + second - 1:] + res
#         # print(paths2)
    
#     if paths1 != [] and paths2 != []:
#         return paths1 + [' '] +  paths2
#     return paths1 + paths2
# print(unique_paths(3, 3))

def unique_paths(m, n, cur=[], first=0, second=0):
    if [first, second] == [m-1, n-1]:
        return [cur[-1]]
    paths1 = []
    paths2 = []

    if second < n - 1:
        res =  unique_paths(m, n, cur+['D'], first, second+1)
        # print(res, cur, 'D')
        # print(first, second)
        if cur != []:
            paths2 = [cur[-1]] + res
        else:
            paths2 = res
        print(cur)
        print(paths2, 'D', '\n')
    if first < m - 1:
        res =  unique_paths(m, n, cur+['R'], first+1, second)
        # print(res, cur, 'R')
        # print(first, second)
        if cur != []:
            paths1 = [cur[-1]] + res
        else:
            paths1 = res
        print(cur)
        print(paths1, "R", '\n')
    
    
    if paths1 != [] and paths2 != []:
        return paths1 + [' '] +  paths2
    return paths1 + paths2
print(unique_paths(3, 3))


