from teamdata import TeamData
import teams

class Teams:
    def __init__(self, teamfile):
        self.teams = {}
        self._get_teams(teamfile)
        #self.calculate_stats()
                    
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
        #for team in self.teams.values():
        #    team.calculate_difficulty_of_schedule(self)


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
                              data.home_team_advantage
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
                print("\n%-5s"%each[2],"%70s"%"W   L   T   Pct    PF   PA  AvMg   Mom  DoS   HA")
                
            print("%-25s"%each[0],"%3d"%each[3],"%3d"%each[4],"%3d"%each[5],\
                  "%6.3f"%each[6],"%4d"%each[7],"%4d"%each[8],"%5.1f"%each[9],\
                  "%5.1f"%each[10],"%4.1f"%each[11],"%4.1f"%each[12])
            count+=1

    def _swap(self,team1,team2):
        temp = team1
        team1 = team2
        team2 = temp        

    def print_games_to_file(self,filename):
        with open(filename,"w") as fout:
            for name,data in self.teams.items():
                fout.write(name+'\n')
                for game in data.games:
                    if game.played == True:
                        fout.write(game.get_gamedata_as_string()+'\n')
                        
    def temp_print(self):
        for team, data in self.teams.items():
            print(team,data.wins, data.losses, data.pct, data.points_for, data.points_against, data.yards_gained, 
                  data.yards_given_up, data.average_margin)
