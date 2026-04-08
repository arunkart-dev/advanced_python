from functools import reduce
nums = [1,2,3,4]
result = reduce(lambda a,b:a if a>b else b,nums)
print(result)