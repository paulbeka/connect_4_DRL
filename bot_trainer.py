import torch
from threading import Thread
from game import Game
from neural_net.agent import Agent

# note: add this to your github

SHOW_TRAINING_PROCESS = True

# play a full game
# determine the winner
# reward winner, punish loser

def train(load_from_file=False):

	# update the screen while the bots are playing
	# need to start a new thread and update the values as if 
	# it were a real player

	n_games = 1

	for gameIndex in range(n_games):

		game = Game()
			
		turn = 0
		i = 0
		while i < 56 and not game.check_victory(game.board):
			players = [Agent(), Agent()]

			game.playMove(turn+1, players[turn].findMove())

			turn = int(not (turn ^ 0)) 		# turn xnor 0
			i += 1

		players[turn].gameFinished(won=True)
		players[int(not turn)].gameFinished(won=False)

		game.playGame()  # For testing
