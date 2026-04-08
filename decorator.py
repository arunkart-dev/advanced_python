def decorator_func(func):
    def wrapper():
        print("Before function runs !")
        func()
        print("After function runs !")
    wrapper()

@decorator_func
def greet():
    print("Hello")





