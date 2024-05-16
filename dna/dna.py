import csv
import sys


store = []


def main():

    # TODO: Check for command-line usage
    if len(sys.argv) != 3:
        print("Usage: Python dna.py csvFile textfile")
        return

    # TODO: Read database file into a variable
    with open(sys.argv[1], "r") as file:
        reader = csv.DictReader(file)
        store = [row for row in reader]

    # TODO: Read DNA sequence file into a variable
    with open(sys.argv[2], "r") as f:
        sequences = f.read()

    # TODO: Find longest match of each STR in DNA sequence
    # longest value dictionary which we will use to store the longest value later on
    longest_value = {}
    # iterating through the first row in store and getting the keys and turning them into list and assigning that to key
    for key in store[0].keys():
        if key == "name":
            continue
        # create a key in longest_value, that will store the longest match value
        longest_value[key] = longest_match(sequences, key)

    # TODO: Check database for matching profile
    # for each row in store
    for row in store:
        # default match to true
        match = True
        # key variable to iterate through the rows and identify the matching largest STR
        for key in row.keys():
            # if the current key is name continue to the next iteration
            if key == "name":
                continue
            # if the key of the current row does not equal the key in longest value
            if int(row[key]) != longest_value[key]:
                # set match to false and break
                match = False
                break
        # if match is true print out the name
        if match == True:
            print(row["name"])
            return
    # else print No match
    print("No match.")


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
