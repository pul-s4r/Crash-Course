print("Starting program")
while True:
    val = input()
    print()
    print("Input string is: {}".format(val))
    print()
    if " " in val:
        print("Not allowed spaces in username")
    elif not val:
        print("Please input a username")
