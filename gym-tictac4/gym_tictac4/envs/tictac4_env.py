import gym
from gym import error, spaces, utils
from gym.utils import seeding

class TicTac4(gym.Env):
	metadata = {'render.modes': ['human']}


	def __init__(self):
		self.state = []
		for i in range(3):
			self.state += [[]]
			for j in range(3):
				self.state[i] += ["-"]
		self.counter = 0
		self.done = 0
		self.add = [0, 0]
		self.reward = 0

	def check(self):

		if(self.counter<5):
			return 0
		for i in range(3):
			if(self.state[i][0] != "-" and self.state[i][1] == self.state[i][0] and self.state[i][1] == self.state[i][2]):
				if(self.state[i][0] == "o"):
					return 1
				else:
					return 2
			if(self.state[0][i] != "-" and self.state[1][i] == self.state[0][i] and self.state[1][i] == self.state[2][i]):
				if(self.state[0][i] == "o"):
					return 1
				else:
					return 2
		if(self.state[0][0] != "-" and self.state[1][1] == self.state[0][0] and self.state[1][1] == self.state[2][2]):
			if(self.state[0][0] == "o"):
				return 1
			else:
				return 2
		if(self.state[0][2] != "-" and self.state[0][2] == self.state[1][1] and self.state[1][1] == self.state[2][0]):
			if(self.state[1][1] == "o"):
				return 1
			else:
				return 2



	def step(self, target):
		if self.done == 1:
			print("Game Over")
			return [self.state, self.reward, self.done, self.add]
		elif self.state[int(target/3)][target%3] != "-":
			print("Invalid Step")
			return [self.state, self.reward, self.done, self.add]
		else:
			if(self.counter%2 == 0):
				self.state[int(target/3)][target%3] = "o"
			else:
				self.state[int(target/3)][target%3] = "x"
			self.counter += 1
			if(self.counter == 9):
				self.done = 1;
			self.render()

		win = self.check()
		if(win):
			self.done = 1;
			print("Player ", win, " wins.", sep = "", end = "\n")
			self.add[win-1] = 1;
			if win == 1:
				self.reward = 100
			else:
				self.reward = -100

		return [self.state, self.reward, self.done, self.add]

	def reset(self):
		for i in range(3):
			for j in range(3):
				self.state[i][j] = "-"
		self.counter = 0
		self.done = 0
		self.add = [0, 0]
		self.reward = 0
		return self.state

	def render(self):
		for i in range(3):
			for j in range(3):
				print(self.state[i][j], end = " ")
			print("")
