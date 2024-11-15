import encrypt as lune

password = input("Enter password: ")
ep = lune.encrypt(password)
dp = lune.decrypt(ep)

print(f"plain : {password}")
print(f"plain -> encrypt : {ep}")
print(f"encrypt -> decrypt : {dp}")