prompt = "\nEnter which topics you would like to add to your pizza: "
prompt += "\n(Remember to enter 'quit' when you are done.) "

message = ""

while message != "quit":
    message = input(prompt)
    if message != "quit":
        print(f"Ok, we will {message} toppings to your pizza.")
