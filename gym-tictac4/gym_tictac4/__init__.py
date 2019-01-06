from gym.envs.registration import register

register(
    id='tictac4-v0',
    entry_point='gym_tictac4.envs:TicTac4',
)