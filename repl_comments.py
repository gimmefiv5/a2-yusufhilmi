input_list = []
a = 1
while True:
    user_input = input("Enter your comment: ")
    input_list.append(user_input)
    print("Previously entered comments: ")
    for x in range(a):
        print((x+1), ". ", input_list[x], sep="")
    a += 1
