import math

def validate(passphrase):
    lower, upper, special, digit = 0, 0, 0, 0
    special_chars = " !\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"

    if passphrase == "":
        print("The passphrase is empty.")
        return False

    for char in passphrase:
        if char.islower():
            lower += 1
        elif char.isupper():
            upper += 1
        elif char in special_chars:
            special += 1
        elif char.isdigit():
            digit += 1

    if lower == 0 or upper == 0 or special == 0 or digit == 0:
        print("The passphrase is invalid.")
        print("It must contain at least one lowercase character, one uppercase character, one special character and one digit.")
        return False
    else:
        return True

def entropy(passphrase):
    combinations = math.pow(95, len(passphrase))
    entropy = math.log(combinations, 2)
    print("The passphrase has an entropy of " + str(entropy) + ".")
    
    if entropy < 80:
        print("This is weak.")
    elif 80 <= entropy < 128:
        print("This is reasonable.")
    elif entropy >= 128:
        print("This is strong.")

if __name__ == "__main__":
    passphrase = input("Please input a passphrase: ")
    if validate(passphrase):
        entropy(passphrase)
