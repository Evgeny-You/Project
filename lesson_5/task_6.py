import timeit


print(timeit.timeit('a = 2 ** 3'))
print(timeit.timeit(('a = 2 + 34 + 56 * 1000')))

