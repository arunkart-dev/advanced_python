class Mycontext:
    def __enter__(self):
        print("Entering context !!")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Existing content !!")


with Mycontext():
    print("Inside block !!")