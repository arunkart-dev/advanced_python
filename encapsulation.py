class Employee:
    def __init__(self,salary):
        self.__salary= salary

    def deposit(self,amount):
        self.__salary +=amount

    def show_balance(self):
        print("Balance : ",self.__salary)

e = Employee(1000)
e.deposit(500)
e.show_balance()
