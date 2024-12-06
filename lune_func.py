"""
Password should not contains wihtespace, backslash, double quotes and single quotes.
"""

import fiw_func as fiw


# Take original password and return encrypted password
def encrypt(password):
    CHARS = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%&()*+,-./:;<=>?@[]^_`{|}~0123456789")
    key = list(get_key())
    encrypted = ""

    for c in password:
        index = CHARS.index(c)
        encrypted += key[index]
    return encrypted


# Take encrypted password and return oringinal password
def decrypt(password):
    CHARS = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%&()*+,-./:;<=>?@[]^_`{|}~0123456789")
    key = list(get_key())
    oringin = ''

    for c in password:
        index = key.index(c)
        oringin += CHARS[index]
    
    return oringin


# Retrun key as str
def get_key():
    key = "kAvG8{]pTa40C9D/+KduE|c;z.BW$[sn>L`7Xw6I~(PV5h-2t?*N<!_1qJljZU3@:Y)^xQSro#}Ff%&Hby=gOeRiMm."
    return key


# Read data from matched username retrun str with comma
def readData(username):
    with open("user_info.txt") as file:
        reader = file.readlines()
        for line in reader:
            data = line.split(',')
            if username == data[0]:
                return line
        else:
            print("Cannot find a matched username")
            return None
        

def showData(data):
    data = data.split(',')
    print('-'*40)
    print(f"|{'Infomation':^38}|")
    print('-'*40)
    print(f"{'| Name':<11}: {data[0]:<26}|")
    if fiw.isMember(data[0]):
        print(f"{'| Status':<11}: {'Member':<26}|")
    else:
        print(f"{'| Status':<11}: {'not Member':<26}|")
    print(f"{'| Balance':<11}: {str(f'{int(data[-2]):,}')+' THB':<26}|")
    print('-'*40)


def manage(menu, amt='', option='', price=''):
    with open("stock.txt") as file:
        reader = file.readlines()
        with open("stock.txt", 'w') as output:
            for line in reader:
                data = line.split(',')
                if menu == data[0]:

                    # Stocks
                    if option != '':
                        if option == 'add':
                            data[-1] = int(data[-1]) + int(amt)
                        elif option == 'sub':
                            data[-1] = int(data[-1]) - int(amt)
                        data[-1] = str(data[-1]) + '\n'

                    # Prices
                    if price != '':
                        data[-2] = price
                        print('da')

                output.write(f"{data[0]},{data[1]},{data[2]},{data[3]},{data[4]}")
        

# orders list must be [str, int]
def buy(orders, username):
    if len(orders) == 0:
        return False
    balance = int(readData(username).split(',')[-2])
    tt_price = 0

    # Calculate total price
    with open("stock.txt") as file:
        reader = file.readlines()
        with open("stock.txt", 'w') as file:
            for line in reader:
                data = line.split(',')
                data[-1] = int(data[-1])
                count = 0
                for order in orders:
                    if order[0] == data[0]:
                        tt_price += int(data[-2]) * order[1]
                        data[-1] = data[-1] - order[1]
                        count += 1
                    if count == len(orders):
                        break
                file.write(f"{data[0]},{data[1]},{data[2]},{data[3]},{data[4]}\n")
                

    # If member discount 10%
    if fiw.isMember(username):
        tt_price = int(tt_price * 0.9)
    
    # If there is not enough money retrun false
    if balance < tt_price:
        return False
    balance = balance - tt_price
    print(f"Total price: {tt_price}")

    # Update current user's balance
    with open("user_info.txt") as file:
        reader = file.readlines()
        with open("user_info.txt", 'w') as file:
            for line in reader:
                data = line.split(',')
                if data[0] == username:
                    data[-2] = balance
                file.write(f"{data[0]},{data[1]},{data[2]},{data[3]},{data[4]}")


def showMenu(type):
    if type not in ['hot', 'iced']:
        print("Incorrect type of menu.")
        return False
    with open("stock.txt") as file:
        reader = file.readlines()
        print('-'*40)
        for line in reader:
            data = line.split(',')
            if type == data[1] and int(data[-1]) > 0:
                print(f"| {data[0].upper():<5} {data[2]:<23} {data[3]} THB |")
        print('-'*40)

                

if __name__ == "__main__":
    showMenu(input('Enter type: ').lower)