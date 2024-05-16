from cs50 import get_float

# Ask how many cents the customer is owed
cents = 0.00
# do while loop for get_float for cents
while True:
    try:
        cents = get_float("Change Owed: ")
        if cents >= 0:
            break
    except ValueError:
        continue
# variable to store cents * 100
cents_ch = round(cents * 100)


coins = 0

while cents_ch > 0:
    # if cents is greater or equal to 25 that means its a quarter
    if cents_ch >= 25:
        cents_ch -= 25
        coins += 1
    # else if cents is greater than or equal to to 10 -=10 and so on....
    elif cents_ch >= 10:
        cents_ch -= 10
        coins += 1
    elif cents_ch >= 5:
        cents_ch -= 5
        coins += 1
    else:
        cents_ch -= 1
        coins += 1
# Print total number of coins to give the customer
print(coins)
