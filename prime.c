#include <cs50.h>
#include <stdio.h>

int main(void)
{
    //declares min and max which the user is going to input
    int min = get_int("Enter minimum: ");
    int max = get_int("Enter maximum: ");
    int flag;

    // here in the first loop we iterate if min is less than max
    for (int i = min; i <= max; i++)
    {
        // default the flag to 1 which means true
        flag = 1;

        // in this iteration we check if 2 <= i / 2 so basically if i / j is divisible we return false
        for (int j = 2; j <= i / 2; j++)
        {
            if (i % j == 0)
            {
                flag = 0;
                break;
            }
        }

        // and finally we check if flag is 1 (which means true) we print the number and then new line
        if (flag == 1 && i > 1)
        {
            printf("%i\n", i);
        }
    }
}