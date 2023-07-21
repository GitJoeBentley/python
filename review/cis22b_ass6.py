#! /usr/bin/python3

"""
This python module is a solution for the CIS22 assignment 6 located at 
http://voyager.deanza.edu/~bentley/cis22b/ass6.html
"""

__author__ = "Joe Bentley, joe.deanza@gmail.com"

class TeamData:
    """ Contains data for each team """
    def __init__(self, conf='', div=''):
        """
        Creates a new team object.  This object will be value for each Teams dictionary item.
        :param conf: the conference for a team
        :param div: the division for a team
        """
        self._conference = conf
        self._division = div
        self._wins = 0
        self._losses = 0
        self._ties = 0

    def games_played(self) -> int:
        """
        :return: the number of games played by a team
        """
        return self._wins + self._losses + self._ties

    def percent(self) -> float:
        """
        :return: the perent of games won by a team
        """
        try:
            pct = (self._wins + 0.5 * self._ties) / self.games_played()
        except ZeroDivisionError:
            pct = 0 
        return pct
        
    def __repr__(self) -> str:
        """
        :return: a formatted string of team statisitics
        """
        return str(self._wins).rjust(5) + str(self._losses).rjust(5) + str(self._ties).rjust(5) + \
            format(self.percent(),'10.3f')
    
    def _sort_key(self) -> float:
        """
        :return: a float value to be used as a sort key to display the standings
        """
        firstCharOfConference = ord(self._conference[0])
        firstCharOfDivision = ord(self._division[0])
        pctInReverseOrder = 1.0 - self.percent()
        return 100.0 * firstCharOfConference + firstCharOfDivision + pctInReverseOrder


class Teams:
    """ Contains a dictionary of team name and team data for each team """
    def __init__(self, teams_file: str, games_file: str):
        """
        Creates a dictionary of team names and data.
        :param teams_file: input file containing conferences, divisions, and team names
        :param games_file: input file containing game data (team names and points scored for each game)
        """
        self._teams = {}
        self.get_teams(teams_file)
        self.get_game_data(games_file)

    def get_teams(self, teams_file: str):
        """ 
        Reads and stores name, division, and conference for each team
        :param teams_file: input file containing conferences, divisions, and team names
        """
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
                self._teams[line] = TeamData(conference, division)

    def get_game_data(self, games_file):
        """ 
        Reads data for each game played.  Determines winner, loser & updates team data
        :param games_file: input file containing team names and points scored in each game
        """
        file = open(games_file)
        for line in file:
            line = line.rstrip()
            if 'Date' not in line:
                team1 = line[7:31].rstrip()
                team2 = line[35:59].rstrip()
                score1 = str(line[72:74])
                score2 = str(line[77:79])
                if score1 > score2:
                    self._teams[team1]._wins += 1
                    self._teams[team2]._losses += 1
                elif score2 > score1:
                    self._teams[team2]._wins += 1
                    self._teams[team1]._losses += 1
                else:
                    self._teams[team1]._ties += 1
                    self._teams[team2]._ties += 1
                    
    def print(self):
        """
        Formats teams dictionary data to print the sorted standings
        """
        sorted_teams = sorted(self._teams.items(),key=lambda x:x[1]._sort_key())
        counter = 0
        for item in sorted_teams:
            if counter % 16 == 0:
                print('\n' + item[1]._conference,'Football Conference')
            if counter % 4 == 0:
                print('\n' + item[1]._division.ljust(5),'Division                W    L    T       Pct')
            print(item[0].ljust(25),item[1])
            counter += 1      


if __name__ == "__main__":
    nfl = Teams('teams.txt', 'scores.txt')
    nfl.print()
