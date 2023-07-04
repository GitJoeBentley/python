#! /usr/bin/python3

# CIS22B - Assignment 6

class Team:
    def __init__(self, name: str, division: str, conference: str):
        self._name = name
        self._division = division
        self._conference = conference
        self._wins = 0
        self._losses = 0
        self._ties = 0 
        self._pct = 0.000

    def __repr__(self):
        return self._name + self._division + self._conference + str(self._wins)

class Teams:
    def __init__(self, teams_file: str, games_file: str):
        self._teams = []
        self.get_teams(teams_file)
        self.get_game_data(games_file)

    def get_teams(self, teams_file: str):
        file = open(teams_file)
        for line in file:
            line = line.rstrip()
            if len(line) < 2:
                continue
            elif 'Conference' in line:
                conference = line[:9]

            elif 'FC' in line:
                division = line[4:]
            else:
                self._teams.append(Team(line,division,conference))

    def get_game_data(self, games_file):
        file = open(games_file)
        for line in file:
            line = line.rstrip()
            if 'Date' not in line:
                team1 = line[7:31].rstrip()
                print(team1)

            

nfl = Teams('teams.txt', 'games.txt')
