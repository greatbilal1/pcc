def add():

    try:
        firstValue = float(input("Enter first value: "))

        secondValue = float(input("Enter second value: "))

    except Exception as e:
        print(e)
    else:
        print(f"Sum of {firstValue} and {secondValue} is {firstValue+secondValue}.")


add()
