#include <cs50.h>
#include <stdio.h>

int height;
int main(void)
{
    do
    {
        height = get_int("Please input height: ");
    }
    while(height < 1 || height > 8);


    for(int i = 0; i < height; i++)
    {
        for(int space = 0; space < height - i - 1; space++)
        {
            printf(" ");
        }
        for(int j = 0; j <= i; j++)
        {
            printf("#");
        }
        for(int k = 0; k <= i; k++)
        {
            printf("#");
        }
        printf("\n");
    }




}