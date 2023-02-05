def build_profile(first, last, **user_info):
    user_info["first_name"] = first.title()
    user_info["last_name"] = last.title()
    return user_info


print(
    build_profile(
        "Alzy", "Welzy", dob="14-07-2002", age=20, nationality="indian".title()
    )
)

print(
    build_profile(
        "Welzy", "Alzy", dob="14-07-2002", age=20, nationality="indian".title()
    )
)

print(
    build_profile(
        "Manvendra", "Rajpoot", dob="14-07-2002", age=20, nationality="indian".title()
    )
)
