# Simulate a sports tournament

import csv
import sys
import random

# Number of simluations to run
N = 1000000


def main():

    # Ensure correct usage
    if len(sys.argv) != 2:
        sys.exit("Usage: python tournament.py FILENAME")

    teams = []
    # TODO: Read teams into memory from file
    # read teams from the csv file
    with open(sys.argv[1], "r") as file:
        # declare reader which reads arguments from the command line
        reader = csv.DictReader(file)
        # loop through reader
        for z in reader:
            # update the rating from string to int
            z.update({'rating': int(z['rating'])})
            # append i to teams
            teams.append(z)

    counts = {}
    # TODO: Simulate N tournaments and keep track of win counts
    # we want to simulate the loop N number of times and i used _ because this loop does not need any variable initialization
    for _ in range(N):
        # create a variable n to store the value that simulate tournament function returns
        n = simulate_tournament(teams)
        # check if n is in counts and if it is increment win count of that player by 1
        if n in counts:
            counts[n] += 1
        else:
            # else if n is not in counts then this is the first time this team is winning so we are basically adding n into the list and giving it the value 1
            counts[n] = 1

    # Print each team's chances of winning, according to simulation
    for team in sorted(counts, key=lambda team: counts[team], reverse=True):
        print(f"{team}: {counts[team] * 100 / N:.1f}% chance of winning")


def simulate_game(team1, team2):
    """Simulate a game. Return True if team1 wins, False otherwise."""
    rating1 = team1["rating"]
    rating2 = team2["rating"]
    probability = 1 / (1 + 10 ** ((rating2 - rating1) / 600))
    return random.random() < probability


def simulate_round(teams):
    """Simulate a round. Return a list of winning teams."""
    winners = []

    # Simulate games for all pairs of teams
    for i in range(0, len(teams), 2):
        if simulate_game(teams[i], teams[i + 1]):
            winners.append(teams[i])
        else:
            winners.append(teams[i + 1])

    return winners


def simulate_tournament(teams):
    """Simulate a tournament. Return name of winning team."""
    t = teams[:]
    # loop through the simulate rounds function until it equals one
    while len(t) != 1:
        # simulate rounds on the teams dictionary
        t = simulate_round(t)
    # once the loop finished return the name of the first team (the team who won)'s name
    return t[0]["team"]


if __name__ == "__main__":
    main()
