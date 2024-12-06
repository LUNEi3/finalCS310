import lune_func as lune


def main():
    ...


def register(username, password):
    with open("user_info.txt", "r") as file:
        for line in file:
            stored_user = line.strip().split(",")
            if username in stored_user:
                print("Username already exists! Try a different one.")
                return False

    with open("user_info.txt", "a") as file:
        file.write(f"{username},{password},{'-'},{'0'},{'user'}\n")
    print("Registration successful!")


def login(username, password):
    with open("user_info.txt", "r") as file:
        for line in file:
            data = line.strip().split(",")
            if data[0] == username and data[1] == password:
                    print("Login successful!")
                    return True
    print("Login Fail...")
    print("Incorrect username or password, please try again.")
    return False
            
    


def reset_password(username):
    # username = input("Enter your username: ")
    new_password = lune.encrypt(input("Enter new password: "))
    try:
        user_found = False
        updated_lines = []
        
        with open("user_info.txt", "r") as file:
            for line in file:
                data = line.strip().split(",")
                if data[0] == username:
                    data[1] = new_password
                    user_found = True
                    print("Password reset successful!")
                updated_lines.append(",".join(data))
        
        if not user_found:
            print(f"Username '{username}' not found.")
            return

        with open("user_info.txt", "w") as file:
            file.write("\n".join(updated_lines) + "\n")
    except FileNotFoundError:
        print("No users are registered yet. Please register first.")
    except Exception as e:
        print(f"An error occurred: {e}")


def isAdmin(username, password):
    with open("user_info.txt", "r") as file:
        for line in file:
            data = line.strip().split(",")
            if data[0] == username and data[1] == password and data[-1] == "admin":
                return True
    return False
        
    

if __name__ == "__main__":
    main()