

# equivelant of do while in python
height = 0
while height > 8 or height < 1:
    try:
        height = int(input("Height: "))
    except ValueError:
        height = int(input("Height: "))


# looping through height then doing the spacing and then printing the hash and new line and spacing then printing hash again
for i in range(height):
    # spacing
    for space in range(height - i - 1):
        print(" ", end="")
    # left alligned staircase
    for j in range(i + 1):
        print("#", end="")
    # space between both
    print("  ", end="")
    # right alligned staircase
    for k in range(i + 1):
        print("#", end="")
    print()
