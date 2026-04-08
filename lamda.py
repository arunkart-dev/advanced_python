add = lambda a,b :a+b
print(add(5,3))

square = lambda x : x*x
print(square(7))

#lamda with maps

nums = [1,2,3,4]
result = list(map(lambda x:x*2,nums))
print(result)