import string
import random

def generate_password(plen):
    s1 = string.ascii_lowercase
    s2 = string.ascii_uppercase
    s3 = string.digits
    s4 = string.punctuation

    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))

    # Shuffle the characters to make it more unique
    random.shuffle(s)

    # Ensure the password length doesn't exceed the available characters
    plen = min(plen, len(s))

    # Generate a unique password
    password = "".join(random.sample(s, plen))

    return password

if __name__ == "__main__":
    plen = int(input("Enter password length: "))
    password = generate_password(plen)
    print("Your unique password is:")
    print(password)
