#include "helpers.h"
#include <math.h>
#include <stdlib.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    //looping through the height and width of image
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            //declaring sum wich takes the color values and get the average
            float sum = (image[i][j].rgbtBlue + image[i][j].rgbtGreen + image[i][j].rgbtRed) / 3.0;

            //rounding the average
            float average = round(sum);

            //copying the averages into teh color values
            int av = average;
            image[i][j].rgbtBlue = av;
            image[i][j].rgbtGreen = av;
            image[i][j].rgbtRed = av;
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    float sepiaRed, sepiaBlue, sepiaGreen;
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            // the equation we were asked to implement for the function to work
            sepiaRed = round(.393 * image[i][j].rgbtRed + .769 * image[i][j].rgbtGreen + .189 * image[i][j].rgbtBlue);
            sepiaGreen = round(.349 * image[i][j].rgbtRed + .686 * image[i][j].rgbtGreen + .168 * image[i][j].rgbtBlue);
            sepiaBlue = round(.272 * image[i][j].rgbtRed + .534 * image[i][j].rgbtGreen + .131 * image[i][j].rgbtBlue);
            //copy the values into image
            image[i][j].rgbtRed = sepiaRed;
            image[i][j].rgbtGreen = sepiaGreen;
            image[i][j].rgbtBlue = sepiaBlue;

            //capping sepiacolor to 255 to prevent integer overflow
            if (sepiaRed > 255)
            {
                image[i][j].rgbtRed = 255;
            }

            if (sepiaGreen > 255)
            {
                image[i][j].rgbtGreen = 255;
            }

            if (sepiaBlue > 255)
            {
                image[i][j].rgbtBlue = 255;
            }
        }

    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    //loop through height and width
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            //checking if j is greater than width  -j - 1
            if (j > width - j - 1)
            {
                break;
            }
            //swapping
            RGBTRIPLE temp = image[i][j];
            image[i][j] = image[i][width - j - 1];
            image[i][width - j - 1] = temp;

        }
    }

    return;
}

// Blur image

void blur(int height, int width, RGBTRIPLE image[height][width])
{
    //declare a variable of type rgbtriple to use for reading from the original array and writing back to it
    RGBTRIPLE copy[height][width];
    for (int hc = 0; hc < height; hc++)
    {
        for (int wc = 0; wc < width; wc++)
        {
            copy[hc][wc] = image[hc][wc];
        }
    }
    for (int i = 0; i < height; i++)
    {


        for (int j = 0; j < width; j++)
        {
            //declaring variables that will be used later on
            int valid_pixels = 0;
            float redsum = 0;
            float greensum = 0;
            float bluesum = 0;
            for (int k =  - 1; k <= 1; k++)
            {
                for (int l = - 1; l <= 1; l++)
                {
                    //check if the current pixel is within the image's boundrarys continue
                    if ((k + i < 0 || k + i > height - 1) || (l + j < 0 || l + j > width - 1))
                    {
                        continue;
                    }
                    //otherwise do as follows:
                    else
                    {
                        redsum += copy[i + k][j + l].rgbtRed;
                        greensum += copy[i + k][j + l].rgbtGreen;
                        bluesum += copy[i + k][j + l].rgbtBlue;
                        valid_pixels++;
                    }
                }
            }
            //copying and rounding the values
            image[i][j] = copy[i][j];
            image[i][j].rgbtRed = round(redsum / (float)valid_pixels);
            image[i][j].rgbtGreen = round(greensum / (float)valid_pixels);
            image[i][j].rgbtBlue = round(bluesum / (float)valid_pixels);


        }
    }

    return;
}
