from game import Game

class TeamData:
    
    def __init__(self, conf='', div=''):
        """ This class contains the conference and division for a team """
        """ and a list of games played by that team """
        """ It also contains calculated statistics for each team """
        self.conference = conf
        self.division = div
        self.games = []
        
        # Calculated statistics
        self.wins = 0
        self.losses = 0
        self.ties = 0
        self.games_played = 0
        self.pct = 0.0
        self.points_for = 0
        self.points_against = 0
        self.yards_gained = 0
        self.yards_given_up = 0
        self.average_yards_delta = 0.0
        self.average_margin = 0
        self.momentum = 0.0
        self.difficulty_of_schedule = 0.0
        self.home_team_advantage = 0.0
        self.strength = 0.0      

    def print_games(self):
        for game in self.games:
            game.print()

    def calculate_strength(self):
        #self.strength = 0.5 * self.average_margin + 0.5 * self.momentum + self.difficulty_of_schedule
        self.strength = 0.4 * self.average_margin + 0.4 * self.momentum + \
            0.2 * self.average_yards_delta * self.games_played / 100.0 + self.difficulty_of_schedule

    def calculate_games_played(self):
        self.games_played = self.wins + self.losses + self.ties

    def calculate_pct(self):
        self.pct = (self.wins + 0.5 * self.ties) / self.games_played

    def calculate_average_margin(self):
        self.average_margin = (self.points_for - self.points_against) / self.games_played        

    def calculate_momentum(self, team: str):
        momentum = 0.0
        denominator = float(self.games_played + 1)
        sum_cofficients = 0.0
        for game in self.games:
            if game.played:
                if game.winner == team:
                    margin = game.winner_score - game.loser_score
                else:
                    margin = game.loser_score - game.winner_score
                coefficient = 1.0 / denominator
                sum_cofficients += coefficient
                momentum += coefficient * margin
                denominator -= 1
        self.momentum = momentum / sum_cofficients

    def calculate_home_team_advantage(self, team: str):
        sum_margins = 0.0
        for game in self.games:
            if game.played:
                if game.winner == team:
                    margin = game.winner_score - game.loser_score
                else:
                    margin = game.loser_score - game.winner_score
                # if home game, add margin to sum_margins
                if (margin > 0 and game.is_a_home_game_for_winner) or (margin < 0 and not game.is_a_home_game_for_winner):
                    sum_margins += margin
                else:
                    sum_margins -= margin
        self.home_team_advantage = sum_margins / self.games_played            

    def calculate_difficulty_of_schedule(self, team, teams):
        sum_of_opponent_average_margin = 0.0
        
        for game in self.games:
            if game.played:
                if game.winner  == team:
                    opponent = game.loser
                else:
                    opponent = game.winner
                sum_of_opponent_average_margin += teams[opponent].average_margin
        self.difficulty_of_schedule += sum_of_opponent_average_margin / self.games_played
