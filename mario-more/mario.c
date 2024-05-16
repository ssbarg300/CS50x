#include <cs50.h>
#include <stdio.h>

int height;
int main(void)
{
    //checking userinput
    do
    {
        printf("Please input height: ");
        scanf("%i", &height);
    }
    while (height < 1 || height > 8);

    //iterating through height
    for (int i = 0; i < height; i++)
    {
        //iterating through height - i - 1 so im always adding 8 - the current hashes
        for (int space = 0; space < height - i - 1; space++)
        {
            printf(" ");
        }
        //iterate through height and printing hash tag
        for (int j = 0; j <= i; j++)
        {
            printf("#");
        }
        //printing the space between the left alligned stair case and the right alligned one
        printf("  ");
        //iterating same as j but here im not making it left alligned
        for (int k = 0; k <= i; k++)
        {
            printf("#");
        }
        printf("\n");
    }
}