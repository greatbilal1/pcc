price = {3: "$10", 12: "$15"}

prompt = "\nEnter your age and we will tell you the price: "
prompt = "\n(If you want to exit the program enter '-1'.) "

age = ""
while age != -1:
    age = int(input(prompt))
    if age != -1:
        if age > 3 and age <= 12:
            print(f"The tickey cost for you is {price.get(3)}")
        elif age > 12:
            print(f"The tickey cost for you is {price.get(12)}")
        else:
            print("You must be older than 3 years to watch this movie.")
