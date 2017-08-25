groceries = ["eggs","milk","chocolate","mac and cheese","pizza","lemonade","chicken","bread","ice cream","avacados"]

#defined grocery_print funtion
def grocery_print(date): #this won't actually happen unless it's called
    print("groceries for" + date)
    for food in groceries:
        print(food)

#call grocery_print function
grocery_print(" friday")
