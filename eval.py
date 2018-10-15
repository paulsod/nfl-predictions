from util import *
from forecast import *

execfile('C:/Users/User/Documents/Coding Projects/NFL Predictions Game/nfl-elo-game-master/nfl-elo-game-master/util.py')
execfile('C:/Users/User/Documents/Coding Projects/NFL Predictions Game/nfl-elo-game-master/nfl-elo-game-master/forecast.py')


# Read historical games from CSV
games = Util.read_games("C:/Users/User/Documents/Coding Projects/NFL Predictions Game/nfl-elo-game-master/nfl-elo-game-master/data/nfl_games.csv")

# Forecast every game
Forecast.forecast(games)

# Evaluate our forecasts against Elo
Util.evaluate_forecasts(games)
