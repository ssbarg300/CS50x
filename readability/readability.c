#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <math.h>

int main(void)
{
    // input
    string text = get_string("Text: ");

    // declaring the variables we will use in the for loop
    int letters = 0;
    int words = 1;
    int sentences = 0;

    //iterate over teh length of text
    for (int i = 0; i < strlen(text); i++)
    {

        //check if the charachter is alphabetical if so increment letter
        if (isalpha(text[i]))
        {
            letters++;
        }

        //otherwise if the charachter is white space increment word
        else if (text[i] == ' ')
        {
            words++;
        }

        // lastly otherwise if text is . ! or ? increment sentence
        else if (text[i] == '.' || text[i] == '!' || text[i] == '?')
        {
            sentences++;
        }
    }
    //here are the math functions you are asked to do
    float L = (float) letters / (float) words * 100;
    float S = (float) sentences / (float) words * 100;

    //declaring an index of the above
    int index = round(0.0588 * L - 0.296 * S - 15.8);


    //checking if the index is less than one then output that text and if index is greater than 16 then output that and so on
    if (index < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (index > 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %i\n", index);
    }



}