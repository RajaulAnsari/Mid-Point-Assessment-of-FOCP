secret="parrot"
while True:
    password=input("Greetings! What is the password? ")
    if password!=secret:
        print("Incorrect! You may try again.")
    else:
        break
print("Correct! You may enter.")