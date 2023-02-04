prompt = "\nEnter which topics you would like to add to your pizza: "
prompt += "\n(Remember to enter 'quit' when you are done.) "

active = True

while active:
    message = input(prompt)
    if message == "quit":
        active = False
    else:
        print(f"Ok, we will add {message} toppings to your pizza.")
