#! /usr/bin/python3

# CIS22B - Assignment 6

class TeamData:
    def __init__(self, conf='', div=''):
        self.conference = conf
        self.division = div
        self.wins = 0
        self.losses = 0
        self.ties = 0

    def calculate_games_played(self) -> int:
        return self.wins + self.losses + self.ties

    def percent(self) -> float:
        return (self.wins + 0.5 * self.ties) / self.games_played
    
    def __repr__(self):
        return self.conference + ' ' + self.division

class Teams:
    def __init__(self, teams_file: str, games_file: str):
        self._teams = {}
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
                self._teams[line] = TeamData(division,conference)
                print(line, self._teams[line])

    def get_game_data(self, games_file):
        file = open(games_file)
        for line in file:
            line = line.rstrip()
            if 'Date' not in line:
                team1 = line[7:31].rstrip()
                team2 = line[35:59].rstrip()
                score1 = str(line[72:74])
                score2 = str(line[77:79])
                print(team1,'   ',team2,' ',score1,score2)

            

nfl = Teams('teams.txt', 'scores.txt')
