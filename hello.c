#include <stdio.h>


int main(void)
{
    char name[50];
    printf("Whats your name: ");
    scanf("%s", name);
    printf("Hello, %s\n", name);
}