shopping_list = []

def add_item():
  new_item = input("What item you wanna add to the list? ")
  shopping_list.append(new_item)

while True:
  add_item()
  ask_another_item = input("Do you want to add another item? ")
  
  if ask_another_item == "yes":
    add_item()
    ask_another_item = input("Do you want to add another item? ")

  elif ask_another_item == "no":
    print(shopping_list)
    break