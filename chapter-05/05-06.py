userAge = int(input("Enter your current age: "))

if type(userAge) is int:
    if userAge < 2:
        print("You are a baby")
    elif userAge >= 2 and userAge < 4:
        print("You are a toddler")
    elif userAge >= 4 and userAge < 13:
        print("You are a kid")
    elif userAge >= 13 and userAge < 20:
        print("You are a teenager")
    elif userAge >= 20 and userAge < 65:
        print("You are an adult")
    elif userAge >= 65:
        print("You are an elder")
    else:
        print("Perhaps I won't have to run")
else:
    print("INVALID INPUT!")
