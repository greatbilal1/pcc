fav_mountains = []

# Program to take name of mountains as inputs (3 times)
for i in range(3):
    inp_mountain = input("Enter a name of mountain: ")
    fav_mountains.append(inp_mountain)

print(f"You have inserted a total of {len(fav_mountains)} mountains in your list.")

fav_mountains.sort()
print(fav_mountains)

fav_mountains.reverse()
print(fav_mountains)
