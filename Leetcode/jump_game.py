seen = set()
def jump(array, pos=0):
    if pos == len(array) - 1:
        return True
    for i in range(1, array[pos] + 1):
        if pos + i < len(array):
            if pos+i not in seen:
                result = jump(array, pos+i)
                seen.add(pos+i)
                if result:
                    return True
    return False
print(jump([3,2,1,0,4]))