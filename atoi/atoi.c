#include <cs50.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

int convert(string input);

int main(void)
{
    string input = get_string("Enter a positive integer: ");

    for (int i = 0, n = strlen(input); i < n; i++)
    {
        if (!isdigit(input[i]))
        {
            printf("Invalid Input!\n");
            return 1;
        }
    }

    // Convert string to int
    printf("%i\n", convert(input));
}

int convert(string input)
{
    // here we declare int i  gets string length of input
    int i = strlen(input);

    // base case
    if (i == 1)
    {
        return input[i - 1] - '0';
    }

    //here we declare num wich is the converted number
    int num = input[i - 1] - '0';

    //we remove the last char and replace it with null
    input[i - 1] = '\0';


    // now we just return the value using recursion
    return num + 10 * convert(input);

}