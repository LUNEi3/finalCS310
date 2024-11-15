
"""
Password should not contains wihtespace, backslash, double quotes and single quotes.
"""

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


# retrun key as str
def get_key():
    key = "kAvG8{]pTa40C9D/+,KduE|c;z.BW$[sn>L`7Xw6I~(PV5h-2t?*N<!_1qJljZU3@:Y)^xQSro#}Ff%&Hby=gOeRiMm"
    return key


# -------------Testing--------------- #
# plain = input("Enter password: ")
# cipher = encrypt(plain)
# op = decrypt(cipher)

# print(f"plain: {plain}")
# print(f"plain->encrypt: {cipher}")
# print(f"cipher->decrypt: {op}")