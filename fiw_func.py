def main():
    # username = 'user2'
    # print(isMember(username))
    username = "admin"
    amt = int(input("จำนวนเงินที่ต้องการเติม: "))
    topup(username, amt)
    

def isMember(username) :
    with open("user_info.txt" , "r") as file1 :
            check_member = file1.read().splitlines()

            for line in check_member :
                data = line.split(",")
                if username == data[0] :
                    if "member" in data[2] :
                        return True
                    if "member" not in data[2] :
                        return False
     

def register_member(username) :
        with open("user_info.txt" , "r") as file1 :
            member_reg = file1.read().splitlines()  

            with open("user_info.txt", "w") as file2:
                for line in member_reg :
                    data = line.split(",")

                    if username == data[0] :
                        line = line.replace('-', 'member')
                        
                    file2.write(f"{line}\n")
        print("Registration successful!")


def topup(username, amt):
    with open("user_info.txt", "r") as file1:
        member_topup = file1.read().splitlines()

    for i in range(len(member_topup)):
        data = member_topup[i].split(",")
        
        if username == data[0]:
            current_balance = int(data[3])

            updated_balance = current_balance + amt

            data[3] = str(updated_balance)
            member_topup[i] = ",".join(data) 

            print("Top-up successful!")
            break

    with open("user_info.txt", "w") as file2:
        for line in member_topup:
            file2.write(f"{line}\n")


if __name__ == "__main__":
    main()