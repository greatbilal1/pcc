pizzas = ["paneer", "chicken", "mushroom"]
friend_pizzas = pizzas[:]
pizzas.append("non-veg")
friend_pizzas.append("cheese")

[print(f"My Pizzas are : {pizza.title()} Pizza") for pizza in pizzas]
[print(f"My Friend Pizzas are : {pizza.title()} Pizza") for pizza in friend_pizzas]
