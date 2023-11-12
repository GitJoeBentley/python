import urllib.request
from game import Game
import teams

class Games:
    """
    This class stores data for all scheduled games (played and unplayed).
    The game data is read in from the web page 'https://www.pro-football-reference.com/years/2023/games.htm'
    """
    
    def __init__(self, NFL, game_data_web_page):
        self.games = []
        pending_week = 0  # first week for unplayed games
        
        data = urllib.request.urlopen(game_data_web_page).read().decode().split('\n')
        for line in data:
            played = False
            if '"week_num"' in line and 'csk' in line:
                # get week number
                pos = line.find('week_num')
                pos = line.find('>',pos + 1)
                pos2 = line.find('<',pos + 1)
                week = int(line[pos+1:pos2])

                # get winning team
                pos = line.find('/teams/', pos2)
                pos = line.find('>', pos)
                pos2 = line.find('<', pos)
                winner  = line[pos + 1:pos2]
                if winner not in NFL.teams:
                    print("Invalid winning team:", winner)

                # get home team is winner (@)
                pos = line.find("game_location", pos2);
                pos = line.find(">", pos);
                is_a_home_game_for_winner = line[pos + 1] != '@'

                # get losing team
                pos = line.find('/teams/', pos2)
                pos = line.find('>', pos)
                pos2 = line.find('<', pos)
                loser  = line[pos + 1:pos2]
                if loser not in NFL.teams:
                    print("Invalid losing team:", loser)

                if line.find("preview", pos2) != -1:
                    if pending_week == 0:
                        pending_week = week
                    winner_score = 0
                    loser_score = 0
                    winner_yards = 0
                    loser_yars = 0
                    is_a_home_game_for_winner = False
                else:
                    # get winner's score
                    pos = line.find("pts_win", pos2)
                    pos = line.find(">", pos + 1);
                    if line[:pos].find("strong"):
                        pos = line.find(">", pos + 1)
                    pos2 = line.find("<", pos)
                    winner_score = int(line[pos + 1: pos2])

                    # get loser's score
                    pos = line.find("pts_lose", pos2);
                    pos = line.find(">", pos + 1);
                    pos2 = line.find("<", pos);
                    loser_score = int(line[pos + 1: pos2])

                    # get winner's yards
                    pos = line.find("yards_win", pos2)
                    pos = line.find(">", pos + 1);
                    pos2 = line.find("<", pos)
                    winner_yards = int(line[pos + 1: pos2])

                    # get loser's yards
                    pos = line.find("yards_lose", pos2)
                    pos = line.find(">", pos + 1);
                    pos2 = line.find("<", pos)
                    loser_yards = int(line[pos + 1: pos2])
                                    
                    NFL.teams[winner].wins = NFL.teams[winner].wins + 1
                    NFL.teams[loser].losses = NFL.teams[loser].losses + 1
                    
                    # points for/against
                    NFL.teams[winner].points_for = NFL.teams[winner].points_for + winner_score
                    NFL.teams[winner].points_against = NFL.teams[winner].points_against + loser_score
                    NFL.teams[loser].points_for = NFL.teams[loser].points_for + loser_score
                    NFL.teams[loser].points_against = NFL.teams[loser].points_against + winner_score
                    
                    # yards gained/given up
                    NFL.teams[winner].yards_gained = NFL.teams[winner].yards_gained + winner_yards
                    NFL.teams[winner].yards_given_up = NFL.teams[winner].yards_given_up + loser_yards
                    NFL.teams[loser].yards_gained = NFL.teams[loser].yards_gained + loser_yards
                    NFL.teams[loser].yards_given_up = NFL.teams[loser].yards_given_up + winner_yards
                    
                    NFL.teams[winner].games_played += 1
                    NFL.teams[loser].games_played += 1

                    played = True

                current_game = Game(week, winner, loser, winner_score, loser_score, winner_yards, loser_yards, is_a_home_game_for_winner, played)
                self.games.append(current_game)
                
                # add game to team's games
                NFL.teams[winner].games.append(current_game)
                NFL.teams[loser].games.append(current_game)

    def get_games(self, team: str) -> [Game]:
        games = []
        for game in self.games:
            if game.winner == team or game.loser == team:
                games.append(game)
        return games
    
    def get_pending_week(self):
        pending_week = 25
        for game in self.games:
            if not game.played and game.week < pending_week:
                pending_week = game.week
        return pending_week;
    
    def get_pending_games(self, pending_week):
        pending_games = []
        
        for game in self.games:
            if game.week == pending_week and not game.played:
                pending_games.append(game)
        return pending_games