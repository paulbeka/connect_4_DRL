import torch
import torch.nn as nn
import torch.nn.functional as F


class Connect4Network(nn.Module):
	def __init__(self):
		super(Connect4Network, self).__init__()

		self.linear1 = nn.Linear(42, 50)
		self.linear2 = nn.Linear(50, 50)
		self.linear3 = nn.Linear(50, 20)
		self.linear4 = nn.Linear(20, 7)

		self.relu = nn.ReLU()

	def forward(self, x):
		x = self.relu(self.linear1(x))
		x = self.relu(self.linear2(x))
		x = self.relu(self.linear3(x))
		x = self.linear4(x)

		return x