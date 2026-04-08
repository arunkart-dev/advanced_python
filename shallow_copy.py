import copy
a = [1,2,[3,4]]
b = copy.copy(a)
b[2][0]= 100
print(a)
print(b)