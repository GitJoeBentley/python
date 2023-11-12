from teamdata import TeamData

class Teams:
    def __init__(self, teamfile):
        self.teams = {}
        self._get_teams(teamfile)
                    
    def _get_teams(self, teamfile):
        with open(teamfile) as fin:
            for line in fin:
                line = line.rstrip()
                if "FC" in line:
                    conf,div = line.split(' ')
                else:
                    self.teams[line] = TeamData(conf,div)

    def calculate_stats(self, games):
        for team, data in self.teams.items():
            self.teams[team].games = games.get_games(team)
            self.teams[team].games_played = len([game for game in self.teams[team].games if game.played])
            data.calculate_pct()
            data.calculate_average_margin()
            data.calculate_momentum(team)
            data.calculate_home_team_advantage(team)
        for team, data in self.teams.items():
            data.calculate_difficulty_of_schedule(team, self.teams)
            data.calculate_strength()

    def sortkey(self,teamdata):
        return ord(teamdata[1][0])*100+ord(teamdata[2][0])+teamdata[6]

    def _sort_for_standings(self,teamslist):
        minIndex = 32
        for i in range(0,len(teamslist)-1):
            minIndex = i
            for j in range(i+1,len(teamslist)):
                if self.sortkey(teamslist[j]) > self.sortkey(teamslist[minIndex]):
                    minIndex = j;
            if minIndex != i:
                temp = teamslist[i]
                teamslist[i] = teamslist[minIndex]
                teamslist[minIndex] = temp
                
    def standings(self):
        # create list of dictionary items
        teamslist = []
        for name,data in self.teams.items():       
            teamslist.append([name,
                              data.conference,
                              data.division,
                              data.wins,
                              data.losses,
                              data.ties,
                              data.pct,
                              data.points_for,
                              data.points_against,
                              data.average_margin,
                              data.momentum,
                              data.difficulty_of_schedule,
                              data.home_team_advantage,
                              data.yards_gained / data.games_played,
                              data.yards_given_up / data.games_played,
                              (data.yards_gained - data.yards_given_up) / data.games_played,
                              data.strength
                              ])
            
        self._sort_for_standings(teamslist)

        count = 0
        for each in teamslist:
            if count % 16 == 0:
                if each[1] == "AFC":
                    print("\nAmerican Football Conference")
                else:
                    print("\nNational Football Conference")
            if count % 4 == 0:
                print("\n%-5s"%each[2],"%91s"%"W   L   T   Pct    PF   PA  AvMg   Mom  DoS   HA  Yd+  Yd-  Yd\u0394   Str")
                
            print("%-25s"%each[0],"%3d"%each[3],"%3d"%each[4],"%3d"%each[5],\
                  "%6.3f"%each[6],"%4d"%each[7],"%4d"%each[8],"%5.1f"%each[9],\
                  "%5.1f"%each[10],"%4.1f"%each[11],"%4.1f"%each[12],
                  "%4.0f"%each[13],"%4.0f"%each[14], "%4.0f"%each[15],
                  "%5.1f"%each[16])
            count+=1

    def _swap(self,team1,team2):
        temp = team1
        team1 = team2
        team2 = temp        

    def print_games_to_file(self,filename):
        with open(filename,"w") as fout:
            for name,data in self.teams.items():
                fout.write(name + '\n')
                for game in data.games:
                    fout.write(str(game) + '\n')
    
    def predictWinner(self, home_team: str, away_team: str) -> str:
        prediction = ''
        homeTS = self.teams[home_team].strength  # home team strength
        awayTS = self.teams[away_team].strength  # home team strength
        
        # get home team advantages
        hta_for_home_team = self.teams[home_team].home_team_advantage
        hta_for_away_team = self.teams[away_team].home_team_advantage
        home_expectation = homeTS + hta_for_home_team / 2.0
        away_expectation = awayTS + hta_for_away_team / 2.0

        margin = home_expectation - away_expectation
        
        if margin > 0.5:
            prediction = home_team + " by " + str(round(abs(margin)))
        elif margin < -0.5:
            prediction = away_team + " by " + str(round(abs(margin)))
        else:
            prediction = "tie";
        return prediction;
