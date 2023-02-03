favnums = {"alzy": [7, 11, 15], "welzy": [3, 9], "alzywelzy": 11}

for user, nums in favnums.items():
    # print(type(nums))
    # print(type(nums) == "list")
    # if type(nums) == "list":
    if type(nums) is list:
        print(f"{user} favorite numbers are:")
        for num in nums:
            print(f"\t\t{num}")
    else:
        print(f"{user} favorite numbers is {nums}")
