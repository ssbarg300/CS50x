// Implements a dictionary's functionality

#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <strings.h>
#include <ctype.h>


#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 26;

// Hash table
node *table[N];

//size of dictionary
int SizeDict = 0;

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // hashv is going to equal the hash value of
    int hashV = hash(word);
    node *cursor = table[hashV];
    while (cursor != NULL)
    {
        //checking if word is equal to cursor word and making it case insensitive by using strcasecmp
        if (strcasecmp(word, cursor->word) == 0)
        {
            return true;
        }
        cursor = cursor->next;
    }
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // the function should return a strings index
    //basically im adding the ascii letters and dividing by N
    int rv = 0;
    for (int i = 0; i < strlen(word); i++)
    {
        //idk why i did it upper i think you can do it lower as well.
        rv += toupper(word[i]);
    }
    //return rv mod n incase rv is greater than n
    return rv % N;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // Declare dp which is gonna be our dictionary and we opened it in read mode
    FILE *dp = fopen(dictionary, "r");
    if (dp == NULL)
    {
        return false;
    }
    char Wordv[LENGTH + 1];
    //here this while loop basically says while this file is being fscanf'd into Wordv and still fscanf doesnt equal to eof do the following:
    while (fscanf(dp, "%s", Wordv) != EOF)
    {
        node *n = malloc(sizeof(node));
        if (n == NULL)
        {
            printf("Hello, dont enter a wrong file again okay :D or i will k*ll you >:>");
            return false;
        }
        //copy wordv into n->word
        strcpy(n->word, Wordv);
        hash(Wordv);
        int hashV = hash(Wordv);
        // put n into hash table at that location
        n->next = table[hashV];
        table[hashV] = n;
        //increment size of dictionary
        SizeDict++;
    }
    fclose(dp);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // return the dictionary size that i incremented in the load function there's two  ways to tackle this but i chose this one.
    return SizeDict;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // TODO
    //loop through the size of n
    for (int i = 0; i < N; i++)
    {
        //declare cursornode
        node *cursor = table[i];
        while (cursor != NULL)
        {
            //use tmp to not lose the linked list in memory i put it outside of the while loop and that resulted in me unloading one word always remember if your iterating through something put it in the loop
            node *tmp = cursor;
            cursor = cursor->next;
            free(tmp);

        }
        //if cursor is null and i is infact n - 1 which is the rightmost boundry to our hash table return true because we are now at the end so there is nothing more to do
        if (cursor == NULL && i == N - 1)
        {
            return true;
        }

    }
    return false;
}