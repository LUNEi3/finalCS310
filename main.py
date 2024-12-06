import first_func as first
import fiw_func as fiw
import lune_func as lune
import sys

title = """| 1. Login                                       |
| 2. Register                                    |
| 3. Exit                                        |"""
title2 = """| 1. Buy                                         |
| 2. Top-up                                      |
| 3. Register a membership                       |
| 4. Reset Password                              |
| 5. Logout                                      | 
| 6. Exit                                        |"""

def main():
    while True:
        while True:
            print("-"*50)
            print(f"|{'Welcome to TaoBin(at home)':^48}|")
            print("-"*50)
            print(title)
            print("-"*50, sep='')
            option = input("Select option(1-3): ").upper()
            if option not in ['1','2','3']:
                print("Incorrect option, please try again...")
                continue

            if option == '3':
                print("Program Exit...")
                sys.exit(0)
            elif option == '2':
                print()
                while True:
                    print("-"*50)
                    print(f"|{'Registration':^48}|")
                    print("-"*50)
                    username = input("Enter your username: ")
                    print("--> Warning: Password should not contains wihtespace, backslash, double quotes and single quotes.")
                    password = lune.encrypt(input("Enter your password: "))
                    print()
                    print("-"*50)
                    if first.register(username, password) != False:
                        print("-"*50)
                        break
                    continue
                continue

            elif option == '1':
                print()
                print("-"*50)
                print(f"|{'Login':^48}|")
                print("-"*50)
                username = input("Enter your username: ")
                # print("--> Warning: Password should not contains wihtespace, backslash, double quotes and single quotes.")
                password = lune.encrypt(input("Enter your password: "))
                if first.login(username, password):
                    break
                else:
                    continue

        if first.isAdmin(username, password):
            admin()
            continue
        input("\nPress Any Key to Continue... ")
        print()

        while True:
            data = lune.readData(username)
            lune.showData(data)
            print("-"*50)
            print(title2)
            print("-"*50)
            option = input("Select option(1-6): ").upper()
            if option not in ['1','2','3','4','5','6']:
                continue

            if option == '6':
                print("Program Exit...")
                sys.exit(0)
            elif option == '5':
                print("Loging out...")
                print()
                break
            elif option == '4':
                print()
                first.reset_password(username)
                continue
            elif option == '3':
                if fiw.isMember(username):
                    print()
                    print("You are a member already.")
                    continue
                sure = input("Are you sure(Y/N): ").upper()
                print()
                if sure == 'Y':
                    fiw.register_member(username)
                    continue
                print("Registration canceled...")
            elif option == '2':
                amt = int(input("Enter amount of money: "))
                print()
                fiw.topup(username, amt)
                continue
            elif option == '1':
                print("Now we currently have only two type of menu (iced, hot)")
                while True:
                    menuType = input("Enter type of menu: ").lower()
                    if menuType not in ['iced', 'hot']:
                        print("Incorrect type, please try again.")
                        continue
                    break
                lune.showMenu(menuType)
                
                # Use loop to get all of order
                orders = []
                print("You can type [C] to cancel.")
                while True:
                    try:
                        menu = input("Enter menu code: ").lower()
                        if menu == 'c':
                            break
                        amt = int(input("Enter amount: "))
                    except ValueError:
                        print("Incorrect amount.")
                        continue
                    
                    orders.append([menu, amt])
                    isContinue = input("Want to order more?(Y/N): ").upper()
                    if isContinue == 'Y':
                        continue
                    break
                print()
                if menu == 'c':
                    print("Order Canceled...")
                    continue
                if lune.buy(orders, username) == False:
                    print()
                    print("You dont't have enough money...")
                    continue
            
title3 = """| 1. Manage                                      |
| 2. Exit                                        |"""
def admin():
    print()
    while True:
        print('-'*50)
        print(f"|{'Admin Command':^48}|")
        print('-'*50)
        print(title3)
        print('-'*50)
        option = input("Select option: ")
        if option == '2':
            print("Exit Admin Mode...")
            break
        elif option == '1':
            with open("stock.txt") as file:
                reader = file.readlines()
                for line in reader:
                    data = line.split(',')
                    print(f"{data[0]:<5}{data[2]:<23}{data[3]:<5}{data[4]}", end='')
            print('-'*50)
            menu = input("Menu code: ")
            op = input("Option(add,sub): ")
            amt = input("Amount: ")
            price = input("Price(Optional): ")
            lune.manage(menu, amt, op, price)
            continue
    print()

main()
