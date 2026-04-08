nums = [1,2,3,4]
matrix = [[1,2],[3,4]]
new = [-3,2,-1,4]
res = [i*2 for i in nums]
cube = [i**3 for i in nums]
zero = [0 if i<0 else i for i in new]
f= [i*i for i in nums]
even = [i for i in nums if i%2==0 ]
odd = [i for i in nums if i%2!=0]
damon = [ "Even" if i%2==0 else "Odd" for i in nums]
ta = [str(i) for i in nums]
flat = [num for row in matrix for num in row]
print(res)
print(f)
print(even)
print(odd)
print(damon)
print(ta)
print(flat)
print(cube)
print(zero)