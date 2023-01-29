guests = ["Akash", "Rajdeep", "Rajveer"]

print(f"Come to dinner, {guests[0]}.")
print(len(guests))
print(f"Total of {len(guests)} are invited.")
print(f"Come to dinner, {guests[1]}.")
print(len(guests))
print(f"Total of {len(guests)} are invited.")
print(f"Come to dinner, {guests[2]}.")
print(len(guests))
print(f"Total of {len(guests)} are invited.")
print(f"{guests[0]} cannot come as he is going out with his girlfriend.")

guests[0] = "Abhishek"

print(f"Come to dinner, {guests[0]}.")
print(len(guests))
print(f"Total of {len(guests)} are invited.")
print(f"Come to dinner, {guests[1]}.")
print(len(guests))
print(f"Total of {len(guests)} are invited.")
print(f"Come to dinner, {guests[2]}.")
print(len(guests))
print(f"Total of {len(guests)} are invited.")

guests.insert(0, "Vishal")
guests.insert(2, "Tarun")
guests.insert(-1, "Madhur")

print(f"Come to dinner, {guests[0]}.")
print(len(guests))
print(f"Total of {len(guests)} are invited.")
print(f"Come to dinner, {guests[1]}.")
print(len(guests))
print(f"Total of {len(guests)} are invited.")
print(f"Come to dinner, {guests[2]}.")
print(len(guests))
print(f"Total of {len(guests)} are invited.")
print(f"Come to dinner, {guests[3]}.")
print(len(guests))
print(f"Total of {len(guests)} are invited.")
print(f"Come to dinner, {guests[4]}.")
print(len(guests))
print(f"Total of {len(guests)} are invited.")
print(f"Come to dinner, {guests[5]}.")
print(len(guests))
print(f"Total of {len(guests)} are invited.")

notInvitedAnymore = guests.pop()
print(f"I'm really sorry but you aren't invited anymore, {notInvitedAnymore}")
notInvitedAnymore = guests.pop()
print(f"I'm really sorry but you aren't invited anymore, {notInvitedAnymore}")
notInvitedAnymore = guests.pop()
print(f"I'm really sorry but you aren't invited anymore, {notInvitedAnymore}")
notInvitedAnymore = guests.pop()
print(f"I'm really sorry but you aren't invited anymore, {notInvitedAnymore}")

print(f"Come to dinner, {guests[0]}.")
print(len(guests))
print(f"Total of {len(guests)} are invited.")
print(f"Come to dinner, {guests[1]}.")
print(len(guests))
print(f"Total of {len(guests)} are invited.")

del guests[0]
del guests[0]

print(guests)

print(len(guests))
print(f"Total of {len(guests)} are invited.")
