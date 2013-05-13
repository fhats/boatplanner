# -*- coding: utf-8 -*-
import testify as T

from boatplanner.logic.lineup import boat_combinations
from boatplanner.logic.lineup import generate_lineup
from boatplanner.logic.lineup import permute_rowers
from boatplanner.models.rower import PORT
from boatplanner.models.rower import STARBOARD
from testing.test_util import make_rower


class GenerateLineupTest(T.TestCase):
	def test_generate_simple_easy_lineup(self):
		rowers = [
			make_rower(height=69, weight=180, sweep_side=PORT, can_scull=True),
			make_rower(height=69, weight=180, sweep_side=STARBOARD, can_scull=True),
			make_rower(height=69, weight=180, sweep_side=PORT, can_scull=True),
			make_rower(height=69, weight=180, sweep_side=STARBOARD, can_scull=True),
			make_rower(height=69, weight=180, sweep_side=PORT, can_scull=True),
			make_rower(height=69, weight=180, sweep_side=STARBOARD, can_scull=True),
			make_rower(height=69, weight=180, sweep_side=PORT, can_scull=True),
			make_rower(height=69, weight=180, sweep_side=STARBOARD, can_scull=True),
		]
		expected_boats = [
			{
				'coxed': True,
				'rowers': rowers,
				'size': 8,
				'sweep': True,
			}
		]

		actual_boats = generate_lineup(rowers)

		T.assert_equal(expected_boats, actual_boats)


class BoatCombinationsTest(T.TestCase):
	def assert_generated_combination(self, num_rowers, expected_combination):
		actual_combination = boat_combinations(num_rowers)
		expected_combination = tuple([tuple(sorted(x)) for x in expected_combination])
		T.assert_equal(sorted(expected_combination), sorted(actual_combination))

	def test_generates_simple_combination(self):
		self.assert_generated_combination(1, [['1x']])

	def test_generates_nothing_no_rowers(self):
		self.assert_generated_combination(0, [[]])

	def test_multiple_boats(self):
		self.assert_generated_combination(2, [['2x'], ['1x', '1x']])

	def test_bigger_lineup(self):
		self.assert_generated_combination(5, [
			['4+'],
			['4x', '1x'],
			['2x', '2x', '1x'],
			['2x', '1x', '1x', '1x'],
			['1x', '1x', '1x', '1x', '1x'],
		])


class PermutationsForBoatsTest(T.TestCase):
	pass  # I'm tired


class PermuteRowersTest(T.TestCase):
	def test_simple_rower_permutation(self):
		rower = make_rower()
		boats = ('1x',)
		expected_permutations = (((rower,),),)
		actual_permutations = permute_rowers([rower], boats)
		T.assert_equal(expected_permutations, actual_permutations)

	def test_three_rower_permutation(self):
		rower1 = make_rower()
		rower2 = make_rower()
		rower3 = make_rower()
		boats = ('2x', '1x')

		expected_permutations = (
			((rower1, rower2), (rower3,)),
			((rower2, rower1), (rower3,)),
			((rower1, rower3), (rower2,)),
			((rower3, rower1), (rower2,)),
			((rower2, rower3), (rower1,)),
			((rower3, rower2), (rower1,)),
		)
		actual_permutations = permute_rowers([rower1, rower2, rower3], boats)

		T.assert_equal(sorted(expected_permutations), sorted(actual_permutations))
