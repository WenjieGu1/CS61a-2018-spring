"""
This is a minimal contest submission file. You may also submit the full
hog.py from Project 1 as your contest entry.

Only this file will be submitted. Make sure to include any helper functions
from `hog.py` that you'll need here! For example, if you have a function to
calculate Free Bacon points, you should make sure it's added to this file
as well.

Don't forget: your strategy must be deterministic and pure.
"""

TEAM_NAME = '' # Change this line!

def final_strategy(score, opponent_score):
    return 5

def play(strategy0, strategy1, score0=0, score1=0, dice=six_sided,
         goal=GOAL_SCORE, say=silence, turn=0, row=0, player=0):
	if score0>=goal or score1>=goal:
		return score0, score1
	else:
        if player==0:
            current_score, c_strategy ,opponent_score= score0, strategy0, score1
        else:
            current_score, c_strategy ,opponent_score= score1, strategy1, score0
        score=take_turn(c_strategy(current_score,opponent_score),opponent_score,dice)
        current_score+=score
        if player == 0:
            score0 = current_score
        else:
            score1 = current_score
        if is_swap(score1,score0):
            score0,score1=score1,score0
        say=say(score0,score1)
        if turn % 8 == c_strategy(current_score,opponent_score) and row == 0:
        	return play(strategy0, strategy1, score0, score1, dice=six_sided,
         goal=GOAL_SCORE, say=silence, turn, row, player)
        else:
        	player=other(player)
        	if row == 1:
        		row = 0
        	turn+=1
        	return play(strategy0, strategy1, score0, score1, dice=six_sided,
         goal=GOAL_SCORE, say=silence, turn, row, player)
