class Game:
    """ This class stores data for each game played."""
    """ A list game objects is intended to be assigned to each team """
    def __init__(self, week: int, winner: str, loser: str, winner_score: int, loser_score: int, 
                 winner_yards: int, loser_yards: int, is_a_home_game_for_winner: bool, played: bool):
        self.week = week
        self.winner = winner
        self.loser = loser
        self.winner_score = winner_score
        self.loser_score = loser_score
        self.winner_yards = winner_yards
        self.loser_yards = loser_yards
        self.is_a_home_game_for_winner = is_a_home_game_for_winner
        self.played = played

    def __str__(self):
        s = str(self.week)
        s = s + ' ' + self.winner + ' ' + str(self.winner_score) + ' ' + self.loser + ' ' + str(self.loser_score) + ' ' + str(self.winner_yards)
        return s
