// Practice writing a function to find a max value

#include <cs50.h>
#include <stdio.h>

int max(int array[], int n);

int main(void)
{
    int n;
    do
    {
        n = get_int("Number of elements: ");
    }
    while (n < 1);

    int arr[n];

    for (int i = 0; i < n; i++)
    {
        arr[i] = get_int("Element %i: ", i);
    }

    printf("The max value is %i.\n", max(arr, n));
}

// TODO: return the max value
int max(int array[], int n)
{
    //here in the function i used linear search

    //the max value equal to array[0] just as a default
    int max_value = array[0];


    for (int i = 0; i < n; i++)
    {
        /*iterate over array and check if any element of the array is greater than the first one,
        if there is one the max value is set to that element if not it stays zero and prints the elements value
        */
        if (array[i] > max_value)
        {
            max_value = array[i];
        }

    }
    //return the max value after.
    return max_value;
}
