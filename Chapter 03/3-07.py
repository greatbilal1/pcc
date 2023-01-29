guests = ["Akash", "Rajdeep", "Rajveer"]

print(f"Come to dinner, {guests[0]}.")
print(f"Come to dinner, {guests[1]}.")
print(f"Come to dinner, {guests[2]}.")
print(f"{guests[0]} cannot come as he is going out with his girlfriend.")

guests[0] = "Abhishek"

print(f"Come to dinner, {guests[0]}.")
print(f"Come to dinner, {guests[1]}.")
print(f"Come to dinner, {guests[2]}.")

guests.insert(0, "Vishal")
guests.insert(2, "Tarun")
guests.insert(-1, "Madhur")

print(f"Come to dinner, {guests[0]}.")
print(f"Come to dinner, {guests[1]}.")
print(f"Come to dinner, {guests[2]}.")
print(f"Come to dinner, {guests[3]}.")
print(f"Come to dinner, {guests[4]}.")
print(f"Come to dinner, {guests[5]}.")

notInvitedAnymore = guests.pop()
print(f"I'm really sorry but you aren't invited anymore, {notInvitedAnymore}")
notInvitedAnymore = guests.pop()
print(f"I'm really sorry but you aren't invited anymore, {notInvitedAnymore}")
notInvitedAnymore = guests.pop()
print(f"I'm really sorry but you aren't invited anymore, {notInvitedAnymore}")
notInvitedAnymore = guests.pop()
print(f"I'm really sorry but you aren't invited anymore, {notInvitedAnymore}")

print(f"Come to dinner, {guests[0]}.")
print(f"Come to dinner, {guests[1]}.")

del guests[0]
del guests[0]

print(guests)
