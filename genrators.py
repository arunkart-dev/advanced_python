# def nums():
#     yield 1
#     yield 2
#     yield 3
#     yield 4
#     yield 5
#     yield 6
#     yield 7
#     yield 8
#     yield 9
#     yield 10
#
# g = nums()
#
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))

#
# def kam():
#     a = (i for i in range(1,11))
#     for i in a:
#         print(i)
# kam()


# def square():
#     b = (i**2 for i in range(1,11))
#     for i in b:
#         print(i)
# square()

# def odd():
#     c= (i for i in range(1,11) if i%2!=0)
#     for i in c:
#         print(i)
# odd()


def fibonacci():
    n = int(input("Enter a number : "))
    a = 0
    b = 1
    for i in range(n):
        print(a)
        c = a+b
        a = b
        b = c
fibonacci()















