def outer():
    x = 10

    def inner():
        print(x)
    return inner

func = outer()
func()
