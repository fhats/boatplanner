# -*- coding: utf-8 -*-
import testify as T

from boatplanner.logic.scoring import all_rowers_row
from testing.test_util import make_rower


class ScoreLineupTest(T.TestCase):
	pass  # Coming soon to a commit near you!


class AllRowersRowTest(T.TestCase):
	def test_true_case(self):
		rower1 = make_rower()
		rower2 = make_rower()
		rower3 = make_rower()
		total_rowers = (rower1, rower2, rower3)
		lineup = ((rower1, rower2, rower3),)

		T.assert_equal(True, all_rowers_row(lineup, total_rowers))

	def test_false_case(self):
		rower1 = make_rower()
		rower2 = make_rower()
		rower3 = make_rower()
		total_rowers = (rower1, rower2, rower3)
		lineup = ((rower1, rower2),)

		T.assert_equal(False, all_rowers_row(lineup, total_rowers))
