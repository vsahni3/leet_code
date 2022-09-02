cache = {}
def f(x):
    if x == 0:
        return '0!'
    start = tuple()
    for i in range(x):
        if i not in cache:
            cache[i] = f(i)
        start += (cache[i],)
    return start
print(f(5))