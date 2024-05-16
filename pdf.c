#include <cs50.h>
#include <stdio.h>
#include <stdint.h>

int main(int argc, string argv[])
{
    if (argc != 2)
    {
        printf("invalid usage\n");
        return 1;
    }
    FILE *input = fopen(argv[1], "r");

    uint8_t buffer[4];
    if(input == NULL)
    {
        printf("No Such File Found\n");
        return 1;
    }

    fread(buffer, 1, 4, input);

    uint8_t Default[] = {37, 80, 68, 70};

    for (int i = 0; i < 4; i++)
    {
        if(buffer[i] != Default[i])
        {
            printf("likely not a pdf\n");
            fclose(input);
            return 0;
        }
    }
    printf("likely a pdf\n");
    fclose(input);
    return 0;
}