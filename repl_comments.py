from hashlib import sha256


def create_hash(password):              # This function is taken from hash_password.py
    pw_bytestring = password.encode()
    return sha256(pw_bytestring).hexdigest()


input_list = []
a = 1

def call_password():
    global hsh1
    pw1 = input('Please enter your password:')  # This line is taken from hash_password
    hsh1 = create_hash(pw1)


while True:
    user_input = input("Enter your comment: ")

    call_password()

    pw_original = "TerriblePassword"             # This line is taken from hash_password.py
    hsh_original = create_hash(pw_original)      # This line is taken from hash_password.py
    if hsh1 == hsh_original:
        input_list.append(user_input)
        print("Previously entered comments: ")
        for x in range(a):
            print((x+1), ". ", input_list[x], sep="")
        a += 1
    else:
        print("I am sorry I can't let you do that.")

