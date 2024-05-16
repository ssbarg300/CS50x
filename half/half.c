// Calculate your half of a restaurant bill
// Data types, operations, type casting, return value

#include <cs50.h>
#include <stdio.h>

float half(float bill, float tax, int tip);

int main(void)
{
    float bill_amount = get_float("Bill before tax and tip: ");
    float tax_percent = get_float("Sale Tax Percent: ");
    int tip_percent = get_int("Tip percent: ");

    printf("You will owe $%.2f each!\n", half(bill_amount, tax_percent, tip_percent));
}

// TODO: Complete the function
float half(float bill, float tax, int tip)
{

   // Convert tax and tip percentages to decimal values
    tax = tax / 100;
    tip = tip / 100;

    // Add tax to bill amount
    float bill_with_tax = bill * (1 + tax);

    // Calculate tip amount
    float tip_amount = bill_with_tax * tip;

    // Calculate total amount, including bill, tax, and tip
    float total_amount = bill_with_tax + tip_amount;

    // Calculate half of total amount and return it
    float half_amount = total_amount / 2;
    return half_amount;
}
