
# ask user for input
text = input("Text: ")


# declare letters, words and sentences we will increment inside the loop
letters = 0.00
words = 1.00
sentences = 0.00

# loop in range of the length of text
for i in range(len(text)):
    # if text is alphabetical increment letters
    if text[i].isalpha():
        letters += 1
    # else if text is equal to white space increment words
    elif text[i] == ' ':
        words += 1
    # else if therese a dot, exclamation mark, or ! increment sentences.
    elif text[i] == '.' or text[i] == '!' or text[i] == '?':
        sentences += 1

# math function for calculating the letters and sentences
l = letters / words * 100
s = sentences / words * 100

# index of the above
index = round(0.0588 * l - 0.296 * s - 15.8)

# check if index is less than one that means your text is before grade 1
if index < 1:
    print("Before Grade 1")
# else if index is greater than 16 then grade 16+
elif index > 16:
    print("Grade 16+")
# else print the grade and index
else:
    print("Grade ", index)
