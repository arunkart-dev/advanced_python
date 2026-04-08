# try:
#     a = int(input("Enter a number 1: "))
#     b = int(input("Enter a number 2: "))
#     result = a/b
#
# except ValueError:
#     print("Value error")
#
# except ZeroDivisionError:
#     print("Zero division error")
#
# else:
#     print("Result : ",result)
#
# finally:
#     print("Exceution completed !!")


try:
    deposit = 1000
    a = int(input("Enter a number for withdraw : "))
    if a > deposit:
        print("Withdawl done")
    else:
        print("Withdraw no !!")
except ValueError:
    print("Value error")

except ZeroDivisionError:
    print("ZeroDivision error !!")

finally:
    print("Executed!!")





