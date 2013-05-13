# -*- coding: utf-8 -*-
"""Implements the logic to generate boat lineups.

In general, lineup generation works like this:

* Count the number of rowers. Figure out the different boat combinations that
  are available.
* For each boat, generate all the permutations of every rower rowing every seat
  of every boat. This is almost certainly something that will need to be made
  smarter since this will definitely blow up with big pools of rowers... but
  I'm too lazy to think about a smart approach right now.
* For each lineup (set of boats), score the lineup overall.
* Order the resulting lineups by score.
* Threshold?

"""
from itertools import permutations

from boatplanner.models.boat import BOAT_SIZES
from boatplanner.models.boat import SIZES_TO_BOAT


def generate_lineup(rowers):
	"""Given an iterable of rowers, generate a proposed lineup of boats."""
	pass


def boat_combinations(num_rowers, head=None, ignore_if_possible=None):
	if not head:
		head = []

	if not ignore_if_possible:
		ignore_if_possible = []

	if num_rowers <= 0:
		return tuple([tuple(sorted(head))])

	combinations = set()

	for boat_size in sorted(SIZES_TO_BOAT.keys(), reverse=True):
		boat_type = SIZES_TO_BOAT[boat_size]
		if boat_size <= num_rowers:
			if boat_type in ignore_if_possible and len(combinations) > 0:
				continue
			new_head = head + [boat_type]
			new_num_rowers = num_rowers - boat_size
			combinations |= set(boat_combinations(new_num_rowers, new_head, ignore_if_possible=ignore_if_possible))

	return tuple(combinations)


def permutations_for_boats(rowers, boats):
	lineups = []
	for boat in boats:
		lineups.extend(permute_rowers(rowers, boat))
	return tuple(lineups)


def permute_rowers(rowers, boats):
	lineups = []
	for rower_list in permutations(rowers):
		current_slice = 0
		lineup = []
		for boat in boats:
			boat_size = BOAT_SIZES[boat]
			next_slice = current_slice + boat_size
			lineup.append(tuple(rower_list[current_slice:next_slice]))
			current_slice = next_slice
		lineups.append(tuple(lineup))
	return tuple(lineups)

