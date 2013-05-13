# -*- coding: utf-8 -*-
from copy import deepcopy


# These should probably live somewhere in a config eventually
SCORE_WEIGHTS = {
	'all_rowers_row': 500,
	'matching_experience': 30,
	'matching_heights': 30,
	'sweep_preferred_side': 5,
	'weight_matches_boat': 10,
}


def score_lineup(lineup, total_rowers):
	"""A bunch of number-fudgy hand-wavy math to figure out what a heuristic
	score for a boat lineup is.
	"""
	score = 0


def all_rowers_row(lineup, total_rowers):
	all_rowers = list(total_rowers)

	for boat in lineup:
		for rower in boat:
			all_rowers.remove(rower)

	return len(all_rowers) == 0
