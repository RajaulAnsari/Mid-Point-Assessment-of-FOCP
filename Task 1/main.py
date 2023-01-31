while True:
    name=input("Greetings! How shall we call you? ")
    if name.startswith("Lord ") or name.startswith("Lady "):
        print("It shall be so, {}".format(name))
        break
    else:
        print("You may not be known by that name!")