from ecomm_service import *

while True:
    print("\n 1. ADD PRODUCT")
    print("2. VIEW PRODUCTS ")
    print("3  UPDATE PRODUCTS ")
    print("4  DELETE PRODUCTS")
    print("5 EXIT")

    choice = int(input("Enter choice : "))

    if choice == 1:
        pname = input("Enter product : ")
        pdescription = input("Enter description : ")
        price = int(input("Enter price : "))
        add_product(pname,pdescription,price)

    elif choice == 2:
        view_product()

    elif choice == 3:
        pid = int(input("Enter product id : "))
        price = int(input("Enter price of product : "))
        update_product(pid,price)

    elif choice == 4:
        pid = int(input("Enter product id : "))
        delete_product(pid)

    elif choice == 5:
        break