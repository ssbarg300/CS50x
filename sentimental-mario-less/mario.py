
# equivelant of do while in python
height = 0
while height > 8 or height < 1:
    try:
        height = int(input("Height: "))
    except ValueError:
        height = int(input("Height: "))


# looping through height then doing the spacing and then printing the hash and new line
for i in range(height):
    for space in range(height - i - 1):
        print(" ", end="")
    for j in range(i + 1):
        print("#", end="")
    print()
