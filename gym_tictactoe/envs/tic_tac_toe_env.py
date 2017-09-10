import functools
import gym
from gym import error, spaces, utils
from gym.utils import seeding


def fulfilled(board):
    return not functools.reduce(lambda x, y: x or y, [' ' in l for l in board])


def won(player, board):
    won_ = False
    n = len(board)
    # look for lines or columns
    i = 0
    while i < n and not won_:
        temp_lin = True
        temp_col = True
        for j in range(n):
            temp_lin &= (board[i][j] == player)
            temp_col &= (board[j][i] == player)
        won_ = (temp_lin or temp_col)
        i += 1
    # look for diagonals
    if not won_:
        i = 0
        temp_main = True
        temp_anti = True
        while i < n:
            temp_main &= (board[i][i] == player)
            temp_anti &= (board[i][n - 1 - i] == player)
            i += 1
        won_ = (temp_main or temp_anti)
    return won_


class TicTacToeEnv(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self):
        self._reset()

    def _step(self, action):
        x, y = action
        if self.board[x][y] != ' ':
            raise Exception('The cell must be empty!')
        self.board[x][y] = self.player
        reward = 0.0
        if won(self.player, self.board):
            self.done = True
            reward = 1.0
        elif fulfilled(self.board):
            self.done = True
            reward = 0.5
        self.player = 'O' if self.player == 'X' else 'X'
        info = None
        observation = self.board
        return observation, reward, self.done, info

    def _reset(self):
        self.board = []
        self.player = 'O'
        self.done = False

    def _render(self, mode='human', close=False):
        print()
        for i in range(len(self.board)):
            print('+---+---+---+')
            print('| {0[0]} | {0[1]} | {0[2]} |'.format(self.board[i]))
        print('+---+---+---+')
        print()
