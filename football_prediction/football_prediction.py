import csv
from games import Games
from teams import Teams


NFL = Teams("data/nfl_teams.txt")
games = Games(NFL, 'https://www.pro-football-reference.com/years/2023/games.htm')
NFL.calculate_stats(games)
#NFL.temp_print()
NFL.standings()
#NFL.print_games_to_file("games.txt")
#for game in NFL.teams['San Francisco 49ers'].games:
#    if game.played:
#        print(game)
