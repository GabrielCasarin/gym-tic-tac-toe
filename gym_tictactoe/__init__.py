from gym.envs.registration import register

register(
    id='tic-tac-toe-v0',
    entry_point='gym_tictactoe.envs:TicTacToeEnv',
)
