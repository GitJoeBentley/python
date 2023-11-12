from games import Games
from teams import Teams
import datetime
import webbrowser 

def predict_pending_games(games: Games, teams: Teams):
    pending_week = games.get_pending_week()
    pending_games = games.get_pending_games(pending_week)
    today = datetime.datetime.now()
    filename = "predictions_week_" + str(pending_week) + today.strftime("_%m%d%y.txt")
    f = open(filename, "w")
    f.write("                          Preditions for Week " + str(pending_week) + '\n\n\n')
    for game in pending_games:
            game_str = '   ' + game.winner + ' at ' + game.loser
            game_str = game_str.ljust(47
                                      )
            f.write(game_str)
            f.write(' ' + teams.predictWinner(game.winner, game.loser) + '\n\n')
    f.close()
    webbrowser.open(filename)

NFL = Teams("data/nfl_teams.txt")
games = Games(NFL, 'https://www.pro-football-reference.com/years/2023/games.htm')
NFL.calculate_stats(games)
NFL.standings()
NFL.print_games_to_file("games.txt")
predict_pending_games(games, NFL)
