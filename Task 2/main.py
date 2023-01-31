no_slices=int(input("How many slices of spam? "))
if no_slices<=1:
    print("Egg with Spam coming up!")
elif no_slices==2:
    print("Egg with Spam and Spam coming up!")
else:
    n="Spam, "*(no_slices-1)
    print("Egg with {}and Spam coming up!".format(n))