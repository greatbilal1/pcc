def add():

    while True:
        print("This is an Addition Calculator. Enter 'q' anytime to exit the program.")

        try:
            firstValue = float(input("Enter first value: "))
            if firstValue == "q":
                break
            secondValue = float(input("Enter second value: "))
            if secondValue == "q":
                break

        except Exception as e:
            print(e)
        else:
            print(f"Sum of {firstValue} and {secondValue} is {firstValue+secondValue}.")


add()
