import csv
import requests


def main():
    # Read NYTimes Covid Database
    download = requests.get(
        "https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv"
    )
    decoded_content = download.content.decode("utf-8")
    file = decoded_content.splitlines()
    reader = csv.DictReader(file)

    # Construct 14 day lists of new cases for each states
    new_cases = calculate(reader)

    # Create a list to store selected states
    states = []
    print("Choose one or more states to view average COVID cases.")
    print("Press enter when done.\n")

    while True:
        state = input("State: ")
        if state in new_cases:
            states.append(state)
        if len(state) == 0:
            break

    print(f"\nSeven-Day Averages")

    # Print out 7-day averages for this week vs last week
    comparative_averages(new_cases, states)


# TODO: Create a dictionary to store 14 most recent days of new cases by state
def calculate(reader):
    new_cases = {}
    previous_cases = {}
    # iterate through reader wich now contains a dictionary of file
    for new_case in reader:
        # set state to the new case state
        state = new_case['state']
        # declaring cases so we can later append it to new_cases
        case = int(new_case['cases'])
        # check if state user enterd is not in new_case
        if state not in new_cases:
            new_cases[state] = []
            previous_cases[state] = 0

        cToday = case - previous_cases[state]
        # append the new case onto the end of the list and
        new_cases[state].append(cToday)
        # my conditional is greater than 14 just for design :D you can also do it == 15 because in theory it should never go greater than 15
        if len(new_cases[state]) > 14:
            # remove the first case out of the queue
            new_cases[state].pop(0)
            # update previous cases to be equal to the  current day's cumulative cases
            previous_cases[state] = case
    # finally return new_cases
    return new_cases


# TODO: Calculate and print out seven day average for given state
def comparative_averages(new_cases, states):

    for i in states:
        # cases list
        cases_list = new_cases[i]
        # calculating last week's average
        lastWeek = int(sum(cases_list[7:]) / 7)
        # calculating first week average
        firstWeek = int(sum(cases_list[:7]) / 7)

        try:
            # try to get the average of weeks
            average = round(((firstWeek - lastWeek) / firstWeek)*100)

        except ZeroDivisionError:
            # if dividing by zero average = 0
            average = 0

        # round last week to the nearest integer
        lastWeek = round(lastWeek)

        # if average is greater then its
        if average > lastWeek:
            inorde = "an increase"
        else:
            inorde = " a decrease"
        print(f"{i} had a 7-day average of {lastWeek} and {inorde} of %{average}.")


main()
