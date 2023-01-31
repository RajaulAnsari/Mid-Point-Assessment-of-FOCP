print("\nWelcome to the shop!")


stock={'apple':35,'banana':18,'orange':26}
fruit=list(stock)
price=list(stock.values())


print("Currently in stock: {} ({}p)-{} ({}p)-{} ({}p)".format(fruit[0],price[0],fruit[1],price[1],fruit[2],price[2]))


print("Pick an Item, or Enter to Checkout.")


brought_item=[]
total_price=[]
while True:
    a=input("Choice--> ")
    if a in stock:
    	brought_item.append(a)
    	print("Item added.")
    	if a=="apple":
    		total_price.append(35)
    	elif a=='banana':
    		total_price.append(18)
    	elif a=='orange':
    		total_price.append(26)
    else:
        print("No such item. Try again")      
    if a=="":
        print("Thank you. You have Purchased {} at a cost {}p".format("-".join(brought_item),sum(total_price)))
        break
