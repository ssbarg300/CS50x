#include <stdio.h>
#include <cs50.h>


int plus;
int main (void)
{

         int starting;
         do
         {
               starting = get_int("please input starting number: ");

         }
         while(starting < 9);

         int ending;
         do
         {
               ending = get_int("Please input an ending number: ");
         }
         while(ending < starting);

         int years = 0;

         while(starting < ending)
         {
               starting += starting / 3 - starting / 4;
               years++;
          }
          printf("Years: %i", years);

}