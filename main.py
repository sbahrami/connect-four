from connect_four import State, Player, Game
from agents import minimax, MinimaxPlayer, zero_heur, three_line_heur, my_heuristic

play_depth = 2

p1 = MinimaxPlayer(play_depth, zero_heur, True)
p2 = MinimaxPlayer(play_depth, zero_heur, True)

game = Game(p1, p2)
game.play_game()
game.display()