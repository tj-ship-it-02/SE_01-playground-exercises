print("Welcome at Pizzafresh Gettorf!")

order_item = input("What would you like to order? ")

if order_item == "":
    print("Sorry, we don't have that item in our menu.")
elif len(order_item) > 15:
    print("Order length is wayyy to long, brev!")
elif order_item == "pizza":
    pizza_type = input("Okay, pizza is a great choice. We got so many great pizzas to choose from. Which one you'd like?")
    pizza_amount = input("How many pizzas would you like to order?")
    pizza_size = input("Which size would you like? Small, Medium, Large?")
    if pizza_size == "Small":
        print("We can't do small pizzas here.")
elif order_item == "salad":
    salad_type = input("Okay, salad is a great choice. We got so many great salads to choose from. Which one you'd like?")
else:
    print("We don't got nothing else, brev!")


