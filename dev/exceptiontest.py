print("Starting program")
while True:
    val = input()
    print()
    print("Input string is: {}".format(val))
    print()
    if not val:
        print("Empty string")
    elif " "in val:
        print("Not allowed space")
    elif val.isspace:
        print("Whitespaces and tabs")
