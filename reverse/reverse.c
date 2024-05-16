#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

#include "wav.h"

int check_format(WAVHEADER header);
int get_block_size(WAVHEADER header);

int main(int argc, char *argv[])
{
    // Ensure proper usage
    // TODO #1
    if (argc != 3)
    {
        printf("Usage: ./reverse filename new_Filename\n");
        return 1;
    }

    // Open input file for reading
    // TODO #2
    FILE *input = fopen(argv[1], "rb");
    if (input == NULL)
    {
        fclose(input);
        printf("Could not open file.\n");
        return 1;
    }

    // Read header
    // TODO #3
    WAVHEADER buffer;
    fread(&buffer, sizeof(WAVHEADER), 1, input);

    // Use check_format to ensure WAV format
    // TODO #4
    if (check_format(buffer) == 1)
    {
        printf("input file format not supported\n");
        return 1;
    }


    // Open output file for writing
    // TODO #5
    FILE *output = fopen(argv[2], "w");
    if (output == NULL)
    {
        fclose(output);
        printf("Could not open file.\n");
        return 1;
    }

    // Write header to file
    // TODO #6
    fwrite(&buffer, sizeof(WAVHEADER), 1, output);
    // Use get_block_size to calculate size of block
    // TODO #7
    int block_size = get_block_size(buffer);

    // Write reversed audio to file
    // declaring an array using malloc lol
    FILE *tempo = malloc(block_size);
    if (fseek(input, block_size, SEEK_END))
    {
        return 1;
    }
    while (ftell(input) - block_size > sizeof(WAVHEADER))
    {
        if (fseek(input, -2 * block_size, SEEK_CUR))
        {
            return 1;
        }
        fread(tempo, block_size, 1, input);
        fwrite(tempo, block_size, 1, output);
    }
    fclose(input);
    fclose(output);
    free(tempo);
}

int check_format(WAVHEADER header)
{
    for (int j = 0; j < 4; j++)
    {
        char wave[4] = {'W', 'A', 'V', 'E'};
        if (header.format[j] == wave[j])
        {
            return 0;
        }
    }
    return 1;
}

int get_block_size(WAVHEADER header)
{
    // TODO #7
    uint16_t bytesPerSample = 0;
    return bytesPerSample = (header.bitsPerSample / 8) * header.numChannels;
}