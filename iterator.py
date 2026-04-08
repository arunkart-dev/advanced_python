# class Count:
#     def __init__(self,max):
#         self.max = max
#         self.num = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.num < self.max:
#             self.num += 1
#             return self.num
#         else:
#             raise StopIteration
#
# c = Count(5)
#
# for  i in c:
#     print(i)

nums = [1,2,3,4]
it = iter(nums)

print(next(it))
print(next(it))
print(next(it))
print(next(it))




