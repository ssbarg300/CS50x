#include <cs50.h>
#include <stdio.h>
#include <string.h>

const int BITS_IN_BYTE = 8;

void print_bulb(int bit);

int main(void)
{
    // ask the user for a message to represent later on as a light bulb
    string message = get_string("Message: ");

    //outer loop itereates over the length of the message
    for (int i = 0, n = strlen(message); i < n; i++)
    {
        //in the outer loop we declare a char called c that is equal to
        int c = message[i];
        int bit[BITS_IN_BYTE] = { 0, 0, 0, 0, 0, 0, 0, 0 };
        for (int j = 0; j < BITS_IN_BYTE; j++)
        {
            if (c % 2 == 1)
            {
                bit[BITS_IN_BYTE - j - 1] = 1;
            }
            c = c / 2;
        }
        for (int k = 0; k < 8; k++)
        {
             print_bulb(bit[k]);
        }
        printf("\n");

    }


}

//print bulb function checks if the bit is zero then light off emoji else if the bit is 1 light emoji
void print_bulb(int bit)
{
    if (bit == 0)
    {
        // Dark emoji
        printf("\U000026AB");
    }
    else if (bit == 1)
    {
        // Light emoji
        printf("\U0001F7E1");
    }
}
