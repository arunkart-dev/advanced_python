nums = [1,2,3,4,5,6]
d = {i:i*i for i in nums}
print(d)

a = [1,2,3]
d2 = {i:str(i)for i in nums}
print(d2)

b = [1,2,3,4,5,6,7]
d1 = {i:i*i for i in b if i%2==0}
print(d1)

c = [1,2,3,4,5]
f = {i:"Even" if i%2==0 else "Odd" for i in nums}
print(f)

s = {'a':1,'b':2,'c':3}
new = {v:k for k,v in s.items()}
print(new)


v= [1,2,3,4]
x = {i:i+10 for i in v}
print(x)

words = ["python","java","ai"]
g = {w:len(w) for w in words}
print(g)




