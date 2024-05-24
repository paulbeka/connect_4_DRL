import pygame, sys


ROW_COUNT = 6
COLUMN_COUNT = 7
SQUARESIZE = 100
RADIUS = int(SQUARESIZE / 2 - 5)
WIDTH = COLUMN_COUNT * SQUARESIZE
HEIGHT = (ROW_COUNT + 1) * SQUARESIZE
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)


pygame.init()


class Game:

	def __init__(self, displayScreen=True):
		self.displayScreen = displayScreen

		self.board = []
		for _ in range(7):
			self.board.append([0]*6)


	def playMove(self, player, col):
		if self.board[col][-1] != 0:
			return None

		i = 0
		while self.board[col][i] != 0:
			i += 1
		self.board[col][i] = player
		return True


	def display(self):
		for c in range(COLUMN_COUNT):
			for r in range(ROW_COUNT):
				pygame.draw.rect(self.screen, BLUE, (c * SQUARESIZE, r * SQUARESIZE + SQUARESIZE, SQUARESIZE, SQUARESIZE))
				if self.board[c][5-r] == 0:
					pygame.draw.circle(self.screen, BLACK, (int(c * SQUARESIZE + SQUARESIZE / 2), int(r * SQUARESIZE + SQUARESIZE + SQUARESIZE / 2)), RADIUS)
				if self.board[c][5-r] == 1:
					pygame.draw.circle(self.screen, RED, (int(c * SQUARESIZE + SQUARESIZE / 2), int(r * SQUARESIZE + SQUARESIZE + SQUARESIZE / 2)), RADIUS)
				if self.board[c][5-r] == 2:
					pygame.draw.circle(self.screen, YELLOW, (int(c * SQUARESIZE + SQUARESIZE / 2), int(r * SQUARESIZE + SQUARESIZE + SQUARESIZE / 2)), RADIUS)

		pygame.display.update()


	def playGame(self):
		if not self.displayScreen:
			return

		p = 1

		self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
		while True:
			self.screen.fill(BLUE)

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()

				if event.type == pygame.KEYDOWN:
					self.playMove(p, int(pygame.key.name(event.key))-1)
					if p == 1:
						p = 2
					else:
						p = 1
			
			self.display()



	def check_victory(self, board):
		for row in range(ROW_COUNT-3):
			for col in range(COLUMN_COUNT):
				if board[col][row] != 0 and board[col][row] == board[col][row + 1] == board[col][row + 2] == board[col][row + 3]:
					return board[col][row]

		for row in range(ROW_COUNT):
			for col in range(COLUMN_COUNT-3):
				if board[col][row] != 0 and board[col][row] == board[col + 1][row] == board[col + 2][row] == board[col + 3][row]:
					return board[col][row]

		for row in range(ROW_COUNT - 3):
			for col in range(COLUMN_COUNT - 3):
				if board[col][row] != 0 and board[col][row] == board[col + 1][row + 1] == board[col + 2][row + 2] == board[col + 3][row + 3]:
					return board[col][row]

		for row in range(3, ROW_COUNT):
			for col in range(COLUMN_COUNT - 3):
				if board[col][row] != 0 and board[col][row] == board[col - 1][row + 1] == board[col - 2][row + 2] == board[col - 3][row + 3]:
					return board[col][row]

		return False
