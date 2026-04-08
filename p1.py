add = lambda a,b : a+b
print(add(8,7))

squares  = lambda x:x**2
print(squares(9))

check = lambda a : a%2==0
print(check(4))

mumbai = [1,2,3,4,5,6,7]
result = list(map(lambda x:x*2,mumbai))
print(result)