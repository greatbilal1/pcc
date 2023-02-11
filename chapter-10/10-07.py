def add(firstValue, secondValue):

    print("This is an Addition Calculator. Enter 'q' anytime to exit the program.")

    try:
        answer = float(firstValue) + float(secondValue)
    except Exception as e:
        print(e)
    else:
        print(f"Sum of {firstValue} and {secondValue} is {answer}.")


while True:
    firstValue = input("Enter first value: ")
    if firstValue == "q":
        break
    secondValue = input("Enter second value: ")
    if secondValue == "q":
        break

    add(firstValue, secondValue)
