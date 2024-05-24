import torch, random
from .network import Connect4Network


class Agent:

	def __init__(self):
		self.brain = Connect4Network()

		self.lr = 0.001

		self.epsilon = 1
		self.optimizer = torch.optim.Adam(self.brain.parameters(), lr=self.lr)


	def findMove(self, board):
		if np.random.rand() < self.epsilon:
			return random.randint(0, 6)
		with torch.no_grad():
			state = torch.tensor(board).flatten()
            values = self.brain(state.float())
            return values.argmax().item()


	def gameFinished(self, won):
		print("gameFinished")

