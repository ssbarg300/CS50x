# this is a list of the valid greetings.
greetings = ["hello", "hello there", "hello, newman"]

#this is what the user will greet the customer with.
greeted = input("Greeting: ")


# here we check if the user greeted with any of the valid greetings.
if greeted.lower().strip() in greetings:
    print("$0")
elif greeted.lower().strip()[0] == "h": # if he did not greet with any valid greeting but his greeting started with an h the bank only has to pay 20 bucks
    print("$20")
else: # else if both conditions are not met than the bank has to pay $100
    print("$100")